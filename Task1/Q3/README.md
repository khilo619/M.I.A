# 🏎️ Voice-Controlled F1 Racing Game

A Python-based Formula 1 racing simulation featuring real-time voice control, where players can control Hassan Mostafa using speech commands while competing against Max Verstappen's AI strategy.

## 🎮 Game Overview

This interactive F1 racing game combines object-oriented programming with voice recognition technology to create an immersive racing experience. Players use voice commands to control Hassan Mostafa's offensive and defensive moves while racing against Max Verstappen's randomized AI strategy.

### ✨ Key Features

- **🎤 Real-time Voice Control**: Control Hassan Mostafa using natural speech commands
- **🤖 AI Opponent**: Max Verstappen uses intelligent random strategy
- **⚔️ Turn-based Combat**: Strategic offensive and defensive move system
- **🛡️ Dynamic Defense**: Real-time damage reduction and blocking mechanics
- **📊 Detailed Combat Feedback**: Clear damage calculations and move descriptions
- **🏁 Multiple Victory Conditions**: Win by tire destruction, fuel depletion, or stalemate
- **🎯 Fallback System**: Automatic random selection if voice recognition fails

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Microphone for voice input
- Internet connection (for Google Speech Recognition)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MIA/Task1/Q3
   ```

2. **Install dependencies**
   ```bash
   pip install SpeechRecognition
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Voice Commands

#### 🔥 Offensive Moves
- **Turbo Start**: Say `"turbo start"` or `"start"`
- **Mercedes Charge**: Say `"mercedes charge"`, `"mercedes"`, or `"charge"`
- **Corner Mastery**: Say `"corner mastery"`, `"corner"`, or `"corner expert"`

#### 🛡️ Defensive Moves
- **Slipstream Cut**: Say `"slipstream cut"`, `"slipstream"`, or `"cut"`
- **Aggressive Block**: Say `"aggressive block"` or `"block"`

### Gameplay Flow

1. **Game starts** with Max Verstappen attacking first
2. **Voice prompts** appear when it's Hassan's turn
3. **10-second reading time** to review available moves
4. **3 attempts** to speak your command clearly
5. **Automatic fallback** to random selection if voice fails
6. **Detailed combat feedback** shows damage dealt and blocked

### Winning Conditions

- 🔥 **Tire Destruction**: Opponent's tire health reaches 0
- ⛽ **Fuel Depletion**: Opponent runs out of fuel
- 🏁 **Stalemate**: Higher tire health wins when both run out of fuel

## 🏗️ Project Structure

```
Q3/
├── main.py              # Main game logic and driver classes
├── speech_handler.py    # Voice recognition and command mapping
├── README.md           # Project documentation
└── __pycache__/        # Python cache (ignored by git)
```

### 📁 File Descriptions

- **`main.py`**: Core game engine with Driver classes, Move system, and Race logic
- **`speech_handler.py`**: Speech recognition handler and voice command mapping system

## 🔧 Technical Details

### Architecture

The game uses **object-oriented design** with the following key components:

#### Core Classes

```python
Driver (ABC)                    # Abstract base class for all drivers
├── MaxVerstappen              # AI-controlled driver with random strategy
└── HassanMostafa              # Voice-controlled driver

Move (ABC)                     # Abstract base class for all moves
├── OffensiveMove              # Attack moves with damage values
└── DefensiveMove              # Defense moves with damage reduction

Race                           # Game controller and turn management
SpeechHandler                  # Voice recognition system
VoiceCommandMapper             # Command translation system
```

#### Game Mechanics

- **Health System**: 100 tire health, 500 fuel capacity
- **Move Costs**: Each move consumes fuel based on complexity
- **Damage Reduction**: Defensive moves reduce incoming damage by percentage
- **Turn Alternation**: Perfect turn-based system with clear feedback

### Voice Recognition

- **Engine**: Google Speech Recognition API
- **Timeout**: 8 seconds per voice command attempt
- **Noise Adjustment**: Automatic background noise calibration
- **Error Handling**: Comprehensive error catching and user feedback

## 🧠 Advanced Technical Analysis

### Object-Oriented Programming Principles

This project demonstrates mastery of all four core OOP principles with sophisticated implementation:

#### 1. 🏗️ **Abstraction**

**Implementation Strategy:**
```python
class Driver(ABC):  # Abstract Base Class
    @abstractmethod
    def choose_offensive_move(self):
        pass
    
    @abstractmethod  
    def choose_defensive_move(self, attack_dmg):
        pass
```

**Design Thinking:**
- **Interface Definition**: The `Driver` class defines the contract that all drivers must follow
- **Implementation Hiding**: Users interact with drivers without knowing internal decision algorithms
- **Behavioral Abstraction**: `choose_offensive_move()` abstracts away whether moves are voice-controlled or AI-generated
- **Complexity Management**: Complex voice recognition logic is hidden behind simple method calls

**Real-World Benefit**: Adding new driver types (e.g., keyboard-controlled, network-controlled) requires only implementing the abstract methods.

#### 2. 🔒 **Encapsulation**

**Private Attributes with Property Decorators:**
```python
class Driver:
    def __init__(self, name, initial_tire_health=100, initial_fuel=500):
        self._name = name           # Private attribute
        self._tire_health = initial_tire_health
        self._fuel = initial_fuel
    
    @property
    def name(self):                # Public getter
        return self._name
    
    @property
    def tire_health(self):
        return self._tire_health
```

**Design Thinking:**
- **Data Protection**: Direct modification of critical game stats prevented
- **Controlled Access**: Properties provide read-only access to internal state
- **Future-Proofing**: Can add validation logic to setters without breaking existing code
- **Information Security**: Internal move lists and voice handlers protected from external manipulation

**Advanced Encapsulation Examples:**
```python
# Protected internal methods
def _validate_move_availability(self, move):
    return self._fuel >= move.fuel_cost

# Encapsulated complex logic
def take_damage(self, damage):
    self._tire_health -= damage
    self._tire_health = max(0, self._tire_health)  # Prevents negative health
```

#### 3. 🧬 **Inheritance**

**Multi-Level Inheritance Hierarchy:**
```python
# Level 1: Abstract Base Classes
class Driver(ABC)
class Move(ABC)

# Level 2: Concrete Implementations  
class MaxVerstappen(Driver)
class HassanMostafa(Driver)
class OffensiveMove(Move)
class DefensiveMove(Move)
```

**Design Thinking:**
- **Code Reusability**: Common driver behavior implemented once in base class
- **Specialization**: Each driver type adds unique behavior while maintaining interface
- **Maintenance Efficiency**: Bug fixes in base class automatically benefit all derived classes
- **Extensibility**: New driver types inherit all base functionality automatically

**Inheritance Benefits Demonstrated:**
```python
# Shared behavior from Driver class
def attack(self, opponent):           # Inherited by both drivers
def defend(self, attack_dmg):         # Common defense mechanism
def take_damage(self, damage):        # Universal damage system

# Specialized behavior in subclasses
class MaxVerstappen(Driver):
    def choose_offensive_move(self):  # AI-based selection
        return random.choice(moves)

class HassanMostafa(Driver):  
    def choose_offensive_move(self):  # Voice-based selection
        return self.voice_recognition_logic()
```

#### 4. 🎭 **Polymorphism**

**Runtime Method Resolution:**
```python
def simulate_turn(self, attacker, defender):
    # Same method call works for any Driver subclass
    offensive_move = attacker.choose_offensive_move()  # Polymorphic call
    defense_move = defender.choose_defensive_move()    # Different implementations
```

**Design Thinking:**
- **Interface Consistency**: Same method calls work regardless of driver type
- **Runtime Flexibility**: Behavior determined by actual object type, not declared type
- **Clean Game Logic**: Race class doesn't need to know if driver is AI or voice-controlled
- **Easy Extension**: New driver types automatically work with existing game logic

**Polymorphism in Action:**
```python
# Both drivers use same interface but different implementations
max_verstappen = MaxVerstappen()     # AI-controlled
hassan_mostafa = HassanMostafa()     # Voice-controlled

# Same method call, different behavior
max_move = max_verstappen.choose_offensive_move()      # → Random selection
hassan_move = hassan_mostafa.choose_offensive_move()   # → Voice recognition
```

### Advanced Design Patterns

#### 🎯 **Strategy Pattern**
**Implementation:**
```python
class VoiceCommandMapper:
    def map_offensive_command(self, voice_command):  # Strategy for voice mapping
    def map_defensive_command(self, voice_command):  # Different strategy for defense
```

**Design Benefit**: Command mapping strategies can be easily swapped or extended.

#### 🏭 **Factory-like Pattern**
**Move Creation:**
```python
self.add_offensive_move(OffensiveMove("DRS Boost", 45, 12, "Description"))
self.add_defensive_move(DefensiveMove("Brake Late", 25, 0.30, "Description"))
```

**Design Benefit**: Centralized move creation with consistent parameter structure.

#### 🔄 **Template Method Pattern**
**Combat Resolution:**
```python
def simulate_turn(self, attacker, defender):
    # Template algorithm that works for any driver types
    offensive_move = attacker.choose_offensive_move()    # Step 1: Attack selection
    defense_move = defender.defend(attack_damage)        # Step 2: Defense resolution  
    defender.take_damage(final_damage)                   # Step 3: Damage application
```

### 🧠 Advanced Programming Concepts

#### **Error Handling & Resilience**
```python
try:
    command = self.recognizer.recognize_google(audio)
    return command.lower()
except sr.WaitTimeoutError:
    return None  # Graceful degradation
except sr.UnknownValueError:
    return None  # Fallback to random selection
```

**Design Philosophy**: System continues functioning even when voice recognition fails.

#### **Composition over Inheritance**
```python
class HassanMostafa(Driver):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        self.speech_handler = SpeechHandler()      # Composition
        self.voice_mapper = VoiceCommandMapper()   # Composition
```

**Design Thinking**: Complex voice functionality added through composition rather than deep inheritance.

#### **Single Responsibility Principle**
- **`Driver`**: Manages driver state and basic actions
- **`SpeechHandler`**: Handles voice recognition only  
- **`VoiceCommandMapper`**: Maps voice to commands only
- **`Race`**: Controls game flow only
- **`Move`**: Encapsulates move logic only

#### **Open/Closed Principle**
```python
# Open for extension (new driver types)
class NewAIDriver(Driver):
    def choose_offensive_move(self):
        return self.machine_learning_selection()

# Closed for modification (existing code unchanged)
race = Race(max_verstappen, new_ai_driver)  # Works immediately
```

#### **Dependency Inversion**
```python
class Race:
    def __init__(self, driver1, driver2):  # Depends on Driver abstraction
        self._driver1 = driver1            # Not concrete implementations
        self._driver2 = driver2
```

### 🎯 Advanced Programming Techniques

#### **Property Decorators for Clean API**
```python
@property
def is_alive(self):
    return self._tire_health > 0 and self._fuel > 0  # Computed property
```

#### **Context Managers for Resource Management**
```python
with self.microphone as source:
    self.recognizer.adjust_for_ambient_noise(source)  # Automatic cleanup
```

#### **Exception Hierarchy Handling**
```python
except sr.WaitTimeoutError:     # Specific timeout handling
except sr.UnknownValueError:    # Specific recognition failure  
except sr.RequestError as e:    # General service errors
```

#### **Dynamic Method Resolution**
```python
# Same method name, different implementations resolved at runtime
attacker.choose_offensive_move()  # Could be AI or voice-controlled
```

### 🚀 Performance & Optimization Considerations

#### **Lazy Initialization**
Voice recognition components only initialized when Hassan is created, not for Max.

#### **Caching Strategy**
Move objects created once during initialization, reused throughout game.

#### **Resource Management**
Microphone resources properly managed with context managers.

#### **Fallback Mechanisms**
Multiple layers of fallback ensure game never breaks:
1. Voice recognition failure → Random selection
2. No available moves → Skip turn
3. Invalid moves → Error handling with retry

### 🎨 Design Philosophy Summary

This project demonstrates **enterprise-level software design** through:

- **Modular Architecture**: Clear separation of concerns
- **Extensible Design**: Easy to add new features without breaking existing code
- **Robust Error Handling**: Graceful degradation under all failure conditions
- **Clean Interfaces**: Simple, intuitive API design
- **Performance Considerations**: Efficient resource usage and response times
- **Maintainable Code**: Clear structure that's easy to debug and modify

The codebase showcases **professional software development practices** suitable for production environments while maintaining **educational clarity** for learning OOP concepts.

## 🎮 Driver Profiles

### 🏎️ Max Verstappen (AI)
**Strategy**: Randomized selection from available moves

**Offensive Moves**:
- **DRS Boost** - Fuel: 45, Damage: 12
- **Red Bull Surge** - Fuel: 80, Damage: 20  
- **Precision Turn** - Fuel: 30, Damage: 8

**Defensive Moves**:
- **Brake Late** - Fuel: 25, 30% damage reduction
- **ERS Deployment** - Fuel: 40, 50% damage reduction (3 uses)

### 🏎️ Hassan Mostafa (Voice-Controlled)
**Strategy**: Player voice commands with intelligent fallback

**Offensive Moves**:
- **Turbo Start** - Fuel: 50, Damage: 10
- **Mercedes Charge** - Fuel: 90, Damage: 22
- **Corner Mastery** - Fuel: 25, Damage: 7

**Defensive Moves**:
- **Slipstream Cut** - Fuel: 20, 40% damage reduction
- **Aggressive Block** - Fuel: 35, 100% damage reduction (2 uses)

## 🛠️ Development

### Dependencies

```python
speech_recognition  # Voice recognition library
random             # AI strategy randomization
time               # Game timing and delays
abc                # Abstract base classes
```

### Code Style

- **PEP 8 compliance** for Python code formatting
- **Comprehensive docstrings** for all major functions
- **Type hints** for better code documentation
- **Object-oriented design** with proper encapsulation

## 🐛 Troubleshooting

### Common Issues

#### Voice Recognition Not Working
```bash
# Check microphone permissions
# Ensure stable internet connection
# Speak clearly and close to microphone
```

#### Installation Problems
```bash
# Update pip
pip install --upgrade pip

# Install with admin rights (if needed)
pip install --user SpeechRecognition
```

#### Game Crashes
```bash
# Check Python version (3.7+ required)
python --version

# Verify all files are present
ls main.py speech_handler.py
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** with proper documentation
4. **Add tests** if applicable
5. **Submit a pull request** with clear description

### Development Setup

```bash
# Clone for development
git clone <repository-url>
cd MIA/Task1/Q3

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install SpeechRecognition
```

## 📝 Project License

This project is developed for educational purposes as part of the MIA coursework.

## 🎯 Future Enhancements

- [ ] **Multiplayer Support**: Voice control for both drivers
- [ ] **Advanced AI**: Strategic AI with learning capabilities
- [ ] **Custom Moves**: Player-defined move creation system
- [ ] **Tournament Mode**: Multi-race championship system
- [ ] **Visual Interface**: GUI with race track visualization
- [ ] **Statistics Tracking**: Player performance analytics
- [ ] **Sound Effects**: Immersive audio experience

## 👥 Authors

- **Khalood** - *Initial development* - Voice-controlled F1 racing system

## 🙏 Acknowledgments

- **Google Speech Recognition** for voice processing capabilities
- **Formula 1** for inspiration and racing terminology
- **Python Community** for excellent documentation and libraries

---

### 🏁 Ready to Race?

Fire up your engines and get ready for an immersive voice-controlled Formula 1 experience!

```bash
python main.py
```

*"Speak your way to victory!"* 🎤🏆
