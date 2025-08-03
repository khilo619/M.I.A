from abc import ABC, abstractmethod 
import random


class Driver(ABC):
    def __init__(self, name, initial_tire_health=100, initial_fuel=500):
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
    def choose_defensive_move(self, attack_dmg):
        pass

    def attack(self, opponent):
        move = self.choose_offensive_move()
        if move:
            return move.execute(self, opponent)
        return f"{self._name} has no available moves!!"
    
    def defend(self, attack_dmg):
        move = self.choose_defensive_move(attack_dmg)
        if move:
            return move.execute(self, attack_dmg)
        return None, attack_dmg, f"{self._name} takes full damage!!"
    
    def take_damage(self,damage):
        self._tire_health -= damage
        self._tire_health = max(0, self._tire_health)



class MaxVerstappen(Driver):
    def __init__(self):
        super().__init__("Max Verstappen")

        self.add_offensive_move(OffensiveMove("DRS Boost", 45, 12, "Drag Reduction System; temporarily increases straight-line speed."))
        self.add_offensive_move(OffensiveMove("Red Bull Surge", 80, 20, "Aggressive acceleration, high tire wear."))
        self.add_offensive_move(OffensiveMove("Precision Turn", 30, 8, "Tactical turn to gain time with minimal fuel use."))


        self.add_defensive_move(DefensiveMove("Brake Late", 25, 0.30, "Uses ultra-late braking to reduce attack impact. Common but risky."))
        self.add_defensive_move(DefensiveMove("ERS Deployment", 40, 0.50, "Deploys electric recovery system defensively to absorb incoming pressure and recover next turn.", 3))


    def choose_offensive_move(self):
        moves = []
        for move in self._offensive_moves:
            if self._fuel >= move.fuel_cost:
                moves.append(move)
        if not moves:
            return None
        

        # go aggressive while you can !!
        if self._fuel > 300:
            best_move = None
            peak_dmg = 0
            for move in moves:
                if move.impact > peak_dmg:
                    peak_dmg = move.impact
                    best_move = move
            return best_move
        
        elif self._fuel < 150:
            best_move = None
            best_efficiency = 0
            for move in moves:
                efficiency = move.impact / move.fuel_cost
                if efficiency > best_efficiency:
                    best_efficiency = efficiency
                    best_move = move
            return best_move
        
        else:
            best_move = None
            best_score = 0
            # I will normalize the scores just to get one finaly balanced score to pick correct needed move
            # normalization here based on values from table
            for move in moves:
                dmg_score = move.impact / 20
                efficiency_score = (move.impact / move.fuel_cost) / 0.3
                best_fuel = (100 - move.fuel_cost) / 100
                balanced_score = (dmg_score + best_fuel + efficiency_score) / 3

                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move

            return best_move



    def choose_defensive_move(self, attack_dmg):
        moves = []
        for move in self._defensive_moves:
            if self._fuel >= move.fuel_cost and move.uses_remaining > 0:
                moves.append(move)
        if not moves:
            return None
        
        if self._tire_health <= attack_dmg:
            best_move = None
            best_def = 0
            for move in moves:
                if move.dmg_reduction > best_def:
                    best_def = move.dmg_reduction
                    best_move = move

            return best_move
        
        elif attack_dmg >= 18:
            best_move = None
            best_def = 0
            for move in moves:
                if move.dmg_reduction >= 0.4: 
                    if move.dmg_reduction > best_def:
                        best_def = move.dmg_reduction
                        best_move = move
            return best_move if best_move else moves[0]  
     
        elif self._fuel < 150:
            best_move = None
            cheapest_cost = float('inf')
            for move in moves:
                if move.fuel_cost < cheapest_cost:
                    cheapest_cost = move.fuel_cost
                    best_move = move
            return best_move
        
        else:
            best_move = None
            best_score = 0
            for move in moves:
                protection_score = move.dmg_reduction / 0.5 
                fuel_efficiency = (100 - move.fuel_cost) / 100 
                balanced_score = (protection_score + fuel_efficiency) / 2
                
                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move
            return best_move



class HassanMostafa(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        
        self.add_offensive_move(OffensiveMove("Turbo Start", 50, 10, "Early burst of speed."))
        self.add_offensive_move(OffensiveMove("Mercedes Charge", 90, 22, "Full-throttle attack."))
        self.add_offensive_move(OffensiveMove("Corner Mastery", 25, 7, "Skilled turning for efficiency."))
        
        self.add_defensive_move(DefensiveMove("Slipstream Cut", 20, 0.40, "Cuts into airflow behind the leading car to limit opponent's advantage and reduce damage."))
        self.add_defensive_move(DefensiveMove("Aggressive Block", 35, 1.00, "Swerves defensively to completely block a single incoming move. Can only be used twice due to high risk.", 2))
    
    def choose_offensive_move(self):
        moves = []
        for move in self._offensive_moves:
            if self._fuel >= move.fuel_cost:
                moves.append(move)
        
        if not moves:
            return None
        
        if self._fuel > 350:
            best_move = None
            peak_dmg = 0
            for move in moves:
                if move.impact > peak_dmg:
                    peak_dmg = move.impact
                    best_move = move
            return best_move
        
        elif self._fuel < 175:
            best_move = None
            best_efficiency = 0
            for move in moves:
                efficiency = move.impact / move.fuel_cost
                if efficiency > best_efficiency:
                    best_efficiency = efficiency
                    best_move = move
            return best_move
        
        else:
            best_move = None
            best_score = 0
            for move in moves:
                dmg_score = move.impact / 22
                efficiency_score = (move.impact / move.fuel_cost) / 0.3
                best_fuel = (100 - move.fuel_cost) / 100
                balanced_score = (dmg_score + best_fuel + efficiency_score) / 3

                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move
            return best_move
    
    def choose_defensive_move(self, attack_dmg):
        moves = []
        for move in self._defensive_moves:
            if self._fuel >= move.fuel_cost and move.uses_remaining > 0:
                moves.append(move)
        
        if not moves:
            return None
        
        if self._tire_health <= attack_dmg:
            best_move = None
            best_def = 0
            for move in moves:
                if move.dmg_reduction > best_def:
                    best_def = move.dmg_reduction
                    best_move = move
            return best_move
        
        elif attack_dmg >= 20:
            best_move = None
            best_def = 0
            for move in moves:
                if move.dmg_reduction >= 0.8:
                    if move.dmg_reduction > best_def:
                        best_def = move.dmg_reduction
                        best_move = move
            return best_move if best_move else moves[0]
        
        elif attack_dmg <= 15:
            best_move = None
            cheapest_cost = float('inf')
            for move in moves:
                if move.fuel_cost < cheapest_cost:
                    cheapest_cost = move.fuel_cost
                    best_move = move
            return best_move
        
        else:
            best_move = None
            best_score = 0
            for move in moves:
                protection_score = move.dmg_reduction / 0.5
                fuel_efficiency = (100 - move.fuel_cost) / 100
                balanced_score = (protection_score + fuel_efficiency) / 2
                
                if balanced_score > best_score:
                    best_score = balanced_score
                    best_move = move
            return best_move


class Move(ABC):
    def __init__ (self, name, fuel_cost, description):
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
    def execute(self, attacker, deffender):
        pass


class OffensiveMove(Move):
    def __init__(self, name, fuel_cost, impact, description):
        super().__init__(name, fuel_cost, description)
        self._impact = impact

    @property
    def impact(self):
        return self._impact
    
    def execute(self, attacker, defender):
        if attacker.fuel >= self._fuel_cost:
            attacker._fuel -= self._fuel_cost
            dmg = self._impact
            defender._tire_health -= dmg
            return f"{attacker.name} used {self._name} to deal {dmg} tire damage to {defender.name}."
        else:
            return f"{attacker.name} can't cast {self._name}!!"


class DefensiveMove(Move):
    def __init__(self, name, fuel_cost, dmg_reduction, description, max_uses = None):
        super().__init__(name, fuel_cost, description)
        self._dmg_reduction = dmg_reduction
        self._max_uses = max_uses
        self._uses_remaining = max_uses if max_uses else float('inf')
    
    @property
    def dmg_reduction(self):
        return self._dmg_reduction
    
    @property
    def uses_remaining(self):
        return self._uses_remaining
    
    def execute(self, defender, attacker_dmg):
        if defender.fuel < self._fuel_cost:
            return None, attacker_dmg, f"{defender.name} can't use {self._name}. Reason: [No enough fuel]"
        if self._uses_remaining <= 0:
            return None, attacker_dmg, f"{defender.name} can't use {self._name}. Reason: [No uses remaining]"
        
        defender._fuel -= self._fuel_cost
        if self._max_uses:
            self._uses_remaining -= 1

        reduced_dmg = max(0, attacker_dmg * (1 - self._dmg_reduction))
        return self, reduced_dmg, f"{defender.name} used {self._name} that reduced the attacker damage from {attacker_dmg} to {reduced_dmg:.1f}"
    

class Race:
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
        
        offensive_move = attacker.choose_offensive_move()
        if not offensive_move:
            print(f"{attacker.name} has no available offensive moves!")
            return
        
        if attacker.fuel < offensive_move.fuel_cost:
            print(f"{attacker.name} doesn't have enough fuel for any moves!")
            return
        
        print(f"{attacker.name} attempts {offensive_move.name}!")
        
        attack_damage = offensive_move.impact
  
        defense_move, final_damage, defense_message = defender.defend(attack_damage)
       
        attacker._fuel -= offensive_move.fuel_cost
        defender.take_damage(final_damage)
        
        print(f"Attack: {offensive_move.name} - {offensive_move.description}")
        print(defense_message)
        print(f"Final damage dealt: {final_damage:.1f}")
    
    def run_race(self):
        print("FORMULA 1 RACE: M.VERSTAPPEN VS H.MOSTAFA")
        print("="*60)
        
        self.print_status()
        
        current_attacker = self._driver1
        current_defender = self._driver2
        consecutive_nomoves = 0  # Track consecutive turns with no moves
        
        while self._driver1.is_alive and self._driver2.is_alive:
            self._round_number += 1
            
            # Check if current attacker can make any move
            available_move = current_attacker.choose_offensive_move()
            if not available_move:
                consecutive_nomoves += 1
                print(f"\n{current_attacker.name}'s turn:")
                print(f"{current_attacker.name} has no available offensive moves!")
                
                # If both players can't move for 2 consecutive turns, it's a stalemate
                if consecutive_nomoves >= 2:
                    print("\n" + "="*60)
                    print("RACE ENDS IN STALEMATE!")
                    print("Both drivers ran out of fuel and cannot continue racing.")
                    print("\n**WINNER BY TIRE HEALTH:**")
                    if self._driver1.tire_health > self._driver2.tire_health:
                        print(f"{self._driver1.name} wins with {self._driver1.tire_health:.1f} tire health!")
                    elif self._driver2.tire_health > self._driver1.tire_health:
                        print(f"{self._driver2.name} wins with {self._driver2.tire_health:.1f} tire health!")
                    else:
                        print("It's a perfect tie! Both drivers have equal tire health!")
                    print(f"Race lasted {self._round_number} rounds.")
                    print("="*60)
                    return
            else:
                consecutive_nomoves = 0
                self.simulate_turn(current_attacker, current_defender)
   
            self.print_status()

            if not current_defender.is_alive:
                break
            
            # toggle turns
            current_attacker, current_defender = current_defender, current_attacker
  
        print("\n" + "="*60)
        print("**RACE RESULTS**")
        if self._driver1.is_alive:
            print(f"WINNER: {self._driver1.name}!")
            print(f"Final Stats - Tire Health: {self._driver1.tire_health}, Fuel: {self._driver1.fuel}")
        else:
            print(f"WINNER: {self._driver2.name}!")
            print(f"Final Stats - Tire Health: {self._driver2.tire_health}, Fuel: {self._driver2.fuel}")
        
        print(f"Race lasted {self._round_number} rounds.")
        print("="*60)


if __name__ == "__main__":
    # Create drivers
    max_verstappen = MaxVerstappen()
    hassan_mostafa = HassanMostafa()
    
    # Create and run race
    race = Race(max_verstappen, hassan_mostafa)
    race.run_race()