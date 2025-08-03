from abc import ABC, abstractmethod
import random

# Abstract base class for moves (Abstraction)
class Move(ABC):
    def __init__(self, name, fuel_cost, description):
        self._name = name
        self._fuel_cost = fuel_cost
        self._description = description
    
    @property
    def name(self):
        return self._name
    
    @property
    def fuel_cost(self):
        return self._fuel_cost
    
    @property
    def description(self):
        return self._description
    
    @abstractmethod
    def execute(self, attacker, defender):
        pass

# Offensive move class (Inheritance)
class OffensiveMove(Move):
    def __init__(self, name, fuel_cost, tire_damage, description):
        super().__init__(name, fuel_cost, description)
        self._tire_damage = tire_damage
    
    @property
    def tire_damage(self):
        return self._tire_damage
    
    def execute(self, attacker, defender):
        if attacker.fuel >= self._fuel_cost:
            attacker._fuel -= self._fuel_cost
            damage = self._tire_damage
            defender._tire_health -= damage
            return f"{attacker.name} uses {self._name}! Deals {damage} tire damage to {defender.name}."
        else:
            return f"{attacker.name} doesn't have enough fuel for {self._name}!"

# Defensive move class (Inheritance)
class DefensiveMove(Move):
    def __init__(self, name, fuel_cost, damage_reduction, description, max_uses=None):
        super().__init__(name, fuel_cost, description)
        self._damage_reduction = damage_reduction
        self._max_uses = max_uses
        self._uses_remaining = max_uses if max_uses else float('inf')
    
    @property
    def damage_reduction(self):
        return self._damage_reduction
    
    @property
    def uses_remaining(self):
        return self._uses_remaining
    
    def execute(self, defender, incoming_damage):
        if defender.fuel < self._fuel_cost:
            return None, incoming_damage, f"{defender.name} cannot use {self._name} - not enough fuel!"
        
        if self._uses_remaining <= 0:
            return None, incoming_damage, f"{defender.name} cannot use {self._name} - no uses remaining!"
        
        defender._fuel -= self._fuel_cost
        if self._max_uses:
            self._uses_remaining -= 1
        
        reduced_damage = max(0, incoming_damage * (1 - self._damage_reduction))
        return self, reduced_damage, f"{defender.name} uses {self._name}! Reduces damage from {incoming_damage} to {reduced_damage:.1f}"

# Abstract Driver class (Abstraction and Encapsulation)
class Driver(ABC):
    def __init__(self, name, initial_tire_health=100, initial_fuel=200):
        self._name = name
        self._tire_health = initial_tire_health
        self._fuel = initial_fuel
        self._offensive_moves = []
        self._defensive_moves = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def tire_health(self):
        return self._tire_health
    
    @property
    def fuel(self):
        return self._fuel
    
    @property
    def is_alive(self):
        return self._tire_health > 0
    
    def add_offensive_move(self, move):
        self._offensive_moves.append(move)
    
    def add_defensive_move(self, move):
        self._defensive_moves.append(move)
    
    @abstractmethod
    def choose_offensive_move(self):
        pass
    
    @abstractmethod
    def choose_defensive_move(self, incoming_damage):
        pass
    
    def attack(self, opponent):
        move = self.choose_offensive_move()
        if move:
            return move.execute(self, opponent)
        return f"{self._name} has no available moves!"
    
    def defend(self, incoming_damage):
        defense = self.choose_defensive_move(incoming_damage)
        if defense:
            return defense.execute(self, incoming_damage)
        return None, incoming_damage, f"{self._name} takes full damage!"
    
    def take_damage(self, damage):
        self._tire_health -= damage
        self._tire_health = max(0, self._tire_health)

# Verstappen class (Inheritance and Polymorphism)
class MaxVerstappen(Driver):
    def __init__(self):
        super().__init__("Max Verstappen")
        
        # Add Verstappen's offensive moves
        self.add_offensive_move(OffensiveMove("DRS Boost", 45, 12, "Drag Reduction System; temporarily increases straight-line speed."))
        self.add_offensive_move(OffensiveMove("Red Bull Surge", 80, 20, "Aggressive acceleration, high tire wear."))
        self.add_offensive_move(OffensiveMove("Precision Turn", 30, 8, "Tactical turn to gain time with minimal fuel use."))
        
        # Add Verstappen's defensive moves
        self.add_defensive_move(DefensiveMove("Brake Late", 25, 0.30, "Uses ultra-late braking to reduce attack impact. Common but risky."))
        self.add_defensive_move(DefensiveMove("ERS Deployment", 40, 0.50, "Deploys electric recovery system defensively to absorb incoming pressure and recover next turn.", 3))
    
    def choose_offensive_move(self):
        # Get all moves we can afford
        available_moves = []
        for move in self._offensive_moves:
            if self._fuel >= move.fuel_cost:
                available_moves.append(move)
        
        if not available_moves:
            return None
        
        # Max's Strategy: Aggressive when fuel is high, efficient when fuel is low
        if self._fuel > 300:
            # Early race - use powerful attacks
            best_move = None
            highest_damage = 0
            for move in available_moves:
                if move.tire_damage > highest_damage:
                    highest_damage = move.tire_damage
                    best_move = move
            return best_move
        
        elif self._fuel < 150:
            # Late race - prioritize fuel efficiency (damage per fuel cost)
            best_move = None
            best_efficiency = 0
            for move in available_moves:
                efficiency = move.tire_damage / move.fuel_cost
                if efficiency > best_efficiency:
                    best_efficiency = efficiency
                    best_move = move
            return best_move
        
        else:
            # Mid race - balanced approach using multi-criteria normalization
            best_move = None
            best_score = 0
            # Normalize scores based on Max's move values for balanced decision making
            for move in available_moves:
                dmg_score = move.tire_damage / 20  # Max damage is 20 (Red Bull Surge)
                efficiency_score = (move.tire_damage / move.fuel_cost) / 0.3  # Max efficiency is ~0.3
                best_fuel = (100 - move.fuel_cost) / 100  # Fuel conservation factor
                balanced_score = (dmg_score + best_fuel + efficiency_score) / 3  # Average of all factors

                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move
            return best_move
    
    def choose_defensive_move(self, incoming_damage):
        # Get all defenses we can use
        available_defenses = []
        for defense in self._defensive_moves:
            if self._fuel >= defense.fuel_cost and defense.uses_remaining > 0:
                available_defenses.append(defense)
        
        if not available_defenses:
            return None
        
        # Max's Strategy: Smart defensive choices
        
        # Emergency situation - about to die
        if self._tire_health <= incoming_damage:
            best_defense = None
            highest_reduction = 0
            for defense in available_defenses:
                if defense.damage_reduction > highest_reduction:
                    highest_reduction = defense.damage_reduction
                    best_defense = defense
            return best_defense
        
        # High damage incoming - use strong defense
        if incoming_damage >= 18:
            for defense in available_defenses:
                if defense.damage_reduction >= 0.5:  # ERS Deployment
                    return defense
        
        # Low fuel - use cheapest defense
        if self._fuel < 60:
            cheapest_defense = None
            lowest_cost = float('inf')
            for defense in available_defenses:
                if defense.fuel_cost < lowest_cost:
                    lowest_cost = defense.fuel_cost
                    cheapest_defense = defense
            return cheapest_defense
        
        # Default - use any available defense
        return available_defenses[0]

# Mostafa class (Inheritance and Polymorphism)
class HassanMostafa(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        
        # Add Mostafa's offensive moves
        self.add_offensive_move(OffensiveMove("Turbo Start", 50, 10, "Early burst of speed."))
        self.add_offensive_move(OffensiveMove("Mercedes Charge", 90, 22, "Full-throttle attack."))
        self.add_offensive_move(OffensiveMove("Corner Mastery", 25, 7, "Skilled turning for efficiency."))
        
        # Add Mostafa's defensive moves
        self.add_defensive_move(DefensiveMove("Slipstream Cut", 20, 0.40, "Cuts into airflow behind the leading car to limit opponent's advantage and reduce damage."))
        self.add_defensive_move(DefensiveMove("Aggressive Block", 35, 1.00, "Swerves defensively to completely block a single incoming move. Can only be used twice due to high risk.", 2))
    
    def choose_offensive_move(self):
        # Get all moves we can afford
        available_moves = []
        for move in self._offensive_moves:
            if self._fuel >= move.fuel_cost:
                available_moves.append(move)
        
        if not available_moves:
            return None
        
        # Hassan's Strategy: Calculated and efficient
        if self._fuel > 350:
            # Early race - use Mercedes Charge for maximum damage
            for move in available_moves:
                if move.name == "Mercedes Charge":
                    return move
            # If Mercedes Charge not available, use highest damage
            best_move = None
            highest_damage = 0
            for move in available_moves:
                if move.tire_damage > highest_damage:
                    highest_damage = move.tire_damage
                    best_move = move
            return best_move
        
        elif self._fuel < 175:
            # Late race - use most efficient moves
            for move in available_moves:
                if move.name == "Corner Mastery":  # Most fuel efficient
                    return move
            # If Corner Mastery not available, find most efficient
            best_move = None
            best_efficiency = 0
            for move in available_moves:
                efficiency = move.tire_damage / move.fuel_cost
                if efficiency > best_efficiency:
                    best_efficiency = efficiency
                    best_move = move
            return best_move
        
        else:
            # Mid race - balanced approach using multi-criteria normalization
            best_move = None
            best_score = 0
            # Normalize scores based on Hassan's move values for balanced decision making
            for move in available_moves:
                dmg_score = move.tire_damage / 22  # Hassan's max damage is 22 (Mercedes Charge)
                efficiency_score = (move.tire_damage / move.fuel_cost) / 0.3  # Max efficiency is ~0.3
                best_fuel = (100 - move.fuel_cost) / 100  # Fuel conservation factor
                balanced_score = (dmg_score + best_fuel + efficiency_score) / 3  # Average of all factors

                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move
            return best_move
    
    def choose_defensive_move(self, incoming_damage):
        # Get all defenses we can use
        available_defenses = []
        for defense in self._defensive_moves:
            if self._fuel >= defense.fuel_cost and defense.uses_remaining > 0:
                available_defenses.append(defense)
        
        if not available_defenses:
            return None
        
        # Hassan's Strategy: Save Aggressive Block for critical moments
        
        # Critical health - use Aggressive Block if available
        if self._tire_health <= 25:
            for defense in available_defenses:
                if defense.name == "Aggressive Block":
                    return defense
        
        # High damage attack - consider using Aggressive Block
        if incoming_damage >= 20:
            for defense in available_defenses:
                if defense.name == "Aggressive Block":
                    return defense
        
        # Finishing move protection - enemy might be going for kill
        opponent_might_finish = incoming_damage >= self._tire_health
        if opponent_might_finish:
            # Use strongest available defense
            best_defense = None
            highest_reduction = 0
            for defense in available_defenses:
                if defense.damage_reduction > highest_reduction:
                    highest_reduction = defense.damage_reduction
                    best_defense = defense
            return best_defense
        
        # Low to moderate damage - use Slipstream Cut (cheaper option)
        if incoming_damage <= 15:
            for defense in available_defenses:
                if defense.name == "Slipstream Cut":
                    return defense
        
        # Default - use cheapest available defense
        cheapest_defense = None
        lowest_cost = float('inf')
        for defense in available_defenses:
            if defense.fuel_cost < lowest_cost:
                lowest_cost = defense.fuel_cost
                cheapest_defense = defense
        return cheapest_defense

# Race simulation class (Encapsulation)
class FormulaOneRace:
    def __init__(self, driver1, driver2):
        self._driver1 = driver1
        self._driver2 = driver2
        self._round_number = 0
    
    def print_status(self):
        print(f"\n--- Round {self._round_number} Status ---")
        print(f"{self._driver1.name}: Tire Health = {self._driver1.tire_health}, Fuel = {self._driver1.fuel}")
        print(f"{self._driver2.name}: Tire Health = {self._driver2.tire_health}, Fuel = {self._driver2.fuel}")
        print("-" * 50)
    
    def simulate_turn(self, attacker, defender):
        print(f"\n{attacker.name}'s turn:")
        
        # Choose offensive move
        offensive_move = attacker.choose_offensive_move()
        if not offensive_move:
            print(f"{attacker.name} has no available offensive moves!")
            return
        
        if attacker.fuel < offensive_move.fuel_cost:
            print(f"{attacker.name} doesn't have enough fuel for any moves!")
            return
        
        print(f"{attacker.name} attempts {offensive_move.name}!")
        
        # Defender chooses defense
        defense_move, final_damage, defense_message = defender.defend(offensive_move.tire_damage)
        
        # Execute attack with potential defense
        attacker._fuel -= offensive_move.fuel_cost
        defender.take_damage(final_damage)
        
        print(f"Attack: {offensive_move.name} - {offensive_move.description}")
        print(defense_message)
        print(f"Final damage dealt: {final_damage:.1f}")
    
    def run_race(self):
        print("🏁 FORMULA 1 RACE: VERSTAPPEN VS MOSTAFA 🏁")
        print("="*60)
        
        self.print_status()
        
        current_attacker = self._driver1
        current_defender = self._driver2
        
        while self._driver1.is_alive and self._driver2.is_alive:
            self._round_number += 1
            
            # Simulate turn
            self.simulate_turn(current_attacker, current_defender)
            
            # Print status after turn
            self.print_status()
            
            # Check win conditions
            if not current_defender.is_alive:
                break
            
            # Switch turns
            current_attacker, current_defender = current_defender, current_attacker
        
        # Print winner
        print("\n" + "="*60)
        print("🏆 RACE RESULTS 🏆")
        if self._driver1.is_alive:
            print(f"🥇 WINNER: {self._driver1.name}!")
            print(f"Final Stats - Tire Health: {self._driver1.tire_health}, Fuel: {self._driver1.fuel}")
        else:
            print(f"🥇 WINNER: {self._driver2.name}!")
            print(f"Final Stats - Tire Health: {self._driver2.tire_health}, Fuel: {self._driver2.fuel}")
        
        print(f"Race lasted {self._round_number} rounds.")
        print("="*60)

# Main execution
if __name__ == "__main__":
    # Create drivers
    max_verstappen = MaxVerstappen()
    hassan_mostafa = HassanMostafa()
    
    # Create and run race
    race = FormulaOneRace(max_verstappen, hassan_mostafa)
    race.run_race()