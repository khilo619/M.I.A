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

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] **Multiplayer Support**: Voice control for both drivers
- [ ] **Advanced AI**: Strategic AI with learning capabilities
- [ ] **Custom Moves**: Player-defined move creation system
- [ ] **Tournament Mode**: Multi-race championship system
- [ ] **Visual Interface**: GUI with race track visualization
- [ ] **Statistics Tracking**: Player performance analytics
- [ ] **Sound Effects**: Immersive audio experience

## 👥 Authors

- **KH&H** - *Initial development* - Voice-controlled F1 racing system

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
