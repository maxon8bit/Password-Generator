# 🔐 Password Generator

A secure and customizable password generator built in Python that creates strong passwords with user-defined criteria.

## ✨ Features

- **Customizable Length**: Generate passwords from 1 to any desired length
- **Character Type Selection**: Choose from lowercase, uppercase, numbers, and symbols
- **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- **Password Strength Checker**: Evaluates and provides feedback on password strength
- **Interactive CLI**: User-friendly command-line interface
- **Multiple Passwords**: Generate multiple passwords in a single session

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maxon8bit/Password-Generator.git
   cd Password-Generator
   ```

2. Run the password generator:
   ```bash
   python main.py
   ```

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only built-in modules)

## 🎯 Usage

Run the program and follow the interactive prompts:

```bash
python main.py
```

### Example Session

```
🔐 Password Generator
==============================

Enter password length (default 12): 16

Character types to include:
Lowercase letters? (Y/n): Y
Uppercase letters? (Y/n): Y
Numbers? (Y/n): Y
Symbols? (Y/n): Y

✅ Generated Password: K#9mP$xL2@qR8wE!
🛡️  Strength: Strong

Generate another password? (Y/n): n

Thanks for using Password Generator!
```

## 🔧 Customization Options

| Option    | Description                              | Default |
|-----------|------------------------------------------|---------|
| Length    | Password length                          | 12      |
| Lowercase | Include a-z                             | Yes     |
| Uppercase | Include A-Z                             | Yes     |
| Numbers   | Include 0-9                             | Yes     |
| Symbols   | Include !@#$%^&*()_+-=[]{}|;:,.<>?     | Yes     |

## 🛡️ Security Features

- Uses `secrets` module for cryptographically secure random number generation
- No password storage or logging
- Immediate password display without file saving
- Secure character selection algorithm

## 📊 Password Strength Levels

- **Very Weak**: Missing multiple character types and/or too short
- **Weak**: Missing some character types
- **Fair**: Basic requirements met
- **Good**: Most security criteria satisfied
- **Strong**: All security criteria met (8+ chars, mixed case, numbers, symbols)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Links

- [Repository](https://github.com/maxon8bit/Password-Generator)
- [Issues](https://github.com/maxon8bit/Password-Generator/issues)

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/maxon8bit/Password-Generator/issues) on GitHub.

---

**⚠️ Security Note**: Always use unique, strong passwords for different accounts and consider using a password manager for secure storage.