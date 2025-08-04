from abc import ABC, abstractmethod 
from speech_handler import SpeechHandler, VoiceCommandMapper
import random
import time


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
        return self._tire_health > 0 and self._fuel > 0  
    
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

        return random.choice(moves)


    def choose_defensive_move(self, attack_dmg):
        moves = []
        for move in self._defensive_moves:
            if self._fuel >= move.fuel_cost and move.uses_remaining > 0:
                moves.append(move)
        
        if not moves:
            return None
     
        return random.choice(moves)
        

class HassanMostafa(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        
        self.add_offensive_move(OffensiveMove("Turbo Start", 50, 10, "Early burst of speed."))
        self.add_offensive_move(OffensiveMove("Mercedes Charge", 90, 22, "Full-throttle attack."))
        self.add_offensive_move(OffensiveMove("Corner Mastery", 25, 7, "Skilled turning for efficiency."))
        
        self.add_defensive_move(DefensiveMove("Slipstream Cut", 20, 0.40, "Cuts into airflow behind the leading car to limit opponent's advantage and reduce damage."))
        self.add_defensive_move(DefensiveMove("Aggressive Block", 35, 1.0, "Swerves defensively to block most incoming damage. Can only be used twice due to high risk.", 2))

        self.speech_handler = SpeechHandler()
        self.voice_mapper = VoiceCommandMapper()


    def choose_offensive_move(self):
        moves = []
        for move in self._offensive_moves:
            if self._fuel >= move.fuel_cost:
                moves.append(move)
        
        if not moves:
            return None
        
        print(f"\n{self.name}'s Available Offensive Moves: ")
        for i, move in enumerate(moves, 1):
            print(f"{i}. {move.name} [Fuel: {move.fuel_cost}, Damage: {move.impact}]")

        # Show only offensive commands
        print("\nAVAILABLE VOICE COMMANDS (OFFENSIVE):")
        print("- Say 'Turbo Start' or 'start'")
        print("- Say 'Mercedes Charge' or 'Mercedes' or 'charge'") 
        print("- Say 'Corner Mastery' or 'Corner' or 'corner expert'")
        print("\nTIP: Speak clearly!!")
        
        # Give player time to read the moves
        print("\n⏰ Take your time to read the moves above...")
        print("💡 You have 10 seconds to decide your strategy!")
        time.sleep(10)

        max_attempts = 3
        for attempt in range(max_attempts):
            print(f"\nAttempt {attempt + 1}/{max_attempts} - Say your offensive move:")
            voice_command = self.speech_handler.listen_for_command()
            if voice_command:
                move_name = self.voice_mapper.map_offensive_command(voice_command)
                if move_name:
                    for move in moves:
                        if move.name == move_name:
                            print(f"✅ Voice command recognized: {move_name}")
                            return move
                    print(f"❌ Move '{move_name}' is not available (insufficient fuel)")
                else:
                     print("❌ Command not recognized. Try again!")

        
        print("⚠️ Voice recognition failed. Using random selection as fallback.")
        return random.choice(moves)
    

    def choose_defensive_move(self, attack_dmg):
        moves = []
        for move in self._defensive_moves:
            if self._fuel >= move.fuel_cost and move.uses_remaining > 0:
                moves.append(move)
        
        if not moves:
            return None
        
        print(f"\n🚨 INCOMING ATTACK: {attack_dmg} damage!")
        print(f"\n{self.name}'s Available Defensive Moves:")
        for i, move in enumerate(moves, 1):
            reduction_percent = int(move.dmg_reduction * 100)
            final_dmg = attack_dmg * (1 - move.dmg_reduction)
            print(f"{i}. {move.name} (Fuel: {move.fuel_cost}, Reduces to {final_dmg:.1f} damage, {reduction_percent}% reduction)")

        # Show only defensive commands
        print("\nAVAILABLE VOICE COMMANDS (DEFENSIVE):")
        print("- Say 'Slipstream Cut' or 'Slipstream' or 'cut'")
        print("- Say 'Aggressive Block' or 'Block'")
        print("\nTIP: Speak clearly!!")
        
        # Give player time to read the defensive options  
        print("\n⏰ URGENT! You have 10 seconds to choose your defense!")
        print("💡 Think quickly about which defense to use!")
        time.sleep(10)
  
        max_attempts = 3
        for attempt in range(max_attempts):
            print(f"\nAttempt {attempt + 1}/{max_attempts} - Say your defensive move:")
            
            voice_command = self.speech_handler.listen_for_command()
            if voice_command:
                move_name = self.voice_mapper.map_defensive_command(voice_command)
                if move_name:
                    # Find the move by name
                    for move in moves:
                        if move.name == move_name:
                            print(f"✅ Voice command recognized: {move_name}")
                            return move
                    print(f"❌ Move '{move_name}' is not available")
                else:
                    print("❌ Command not recognized. Try again!")
            

        print("⚠️ Voice recognition failed. Using random selection as fallback.")
        return random.choice(moves)

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
        
        # Show which defender is about to defend
        print(f"\n🛡️ {defender.name} prepares to defend against {attack_damage} damage...")
  
        defense_move, final_damage, defense_message = defender.defend(attack_damage)
       
        attacker._fuel -= offensive_move.fuel_cost
        defender.take_damage(final_damage)
        
        print(f"\n📊 COMBAT SUMMARY:")
        print(f"Attack: {offensive_move.name} - {offensive_move.description}")
        print(defense_message)
        if defense_move:
            reduction_amount = attack_damage - final_damage
            print(f"🛡️ Defense blocked {reduction_amount:.1f} damage!")
        print(f"💥 Final damage dealt: {final_damage:.1f}")
        
        # Check if attacker ran out of fuel after the move
        if attacker.fuel <= 0:
            print(f"💀 {attacker.name} ran out of fuel and is eliminated!")
        
        # Check if defender died from damage or ran out of fuel
        if defender.tire_health <= 0:
            print(f"💀 {defender.name}'s tires are destroyed!")
        elif defender.fuel <= 0:
            print(f"💀 {defender.name} ran out of fuel and is eliminated!")
    
    def run_race(self):
        print("FORMULA 1 RACE: M.VERSTAPPEN VS H.MOSTAFA")
        print("="*60)
        print("🎤 VOICE CONTROL ENABLED!")
        print(f"📢 {self._driver2.name} will be controlled by voice commands")
        print(f"🤖 {self._driver1.name} uses AI (random strategy)")
        print("="*60)
        
        self.print_status()
        
        current_attacker = self._driver1
        current_defender = self._driver2
        consecutive_nomoves = 0  # Track consecutive turns with no moves
        
        while self._driver1.is_alive and self._driver2.is_alive:
            self._round_number += 1
            
            # Simply run the turn without pre-checking
            consecutive_nomoves = 0
            self.simulate_turn(current_attacker, current_defender)
   
            self.print_status()

            # Check win conditions - if either driver is eliminated
            if not self._driver1.is_alive or not self._driver2.is_alive:
                break
            
            # toggle turns
            current_attacker, current_defender = current_defender, current_attacker
  
        print("\n" + "="*60)
        print("**RACE RESULTS**")
        if self._driver1.is_alive:
            print(f"🏆 WINNER: {self._driver1.name}!")
            print(f"Final Stats - Tire Health: {self._driver1.tire_health}, Fuel: {self._driver1.fuel}")
            
            # Explain why the other driver lost
            if self._driver2.tire_health <= 0:
                print(f"💀 {self._driver2.name} lost due to tire destruction!")
            elif self._driver2.fuel <= 0:
                print(f"⛽ {self._driver2.name} lost due to running out of fuel!")
                
        else:
            print(f"🏆 WINNER: {self._driver2.name}!")
            print(f"Final Stats - Tire Health: {self._driver2.tire_health}, Fuel: {self._driver2.fuel}")
          
            if self._driver1.tire_health <= 0:
                print(f"💀 {self._driver1.name} lost due to tire destruction!")
            elif self._driver1.fuel <= 0:
                print(f"⛽ {self._driver1.name} lost due to running out of fuel!")
        
        print(f"Race lasted {self._round_number} rounds.")
        print("="*60)


if __name__ == "__main__":
    # Create drivers
    max_verstappen = MaxVerstappen()
    hassan_mostafa = HassanMostafa()
    
    # Create and run race
    race = Race(max_verstappen, hassan_mostafa)
    race.run_race()