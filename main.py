import random
import string
import secrets

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length=12, use_lowercase=True, use_uppercase=True, 
                         use_digits=True, use_symbols=True):
        """Generate a secure password with specified criteria."""
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        # Build character set based on options
        chars = ""
        if use_lowercase:
            chars += self.lowercase
        if use_uppercase:
            chars += self.uppercase
        if use_digits:
            chars += self.digits
        if use_symbols:
            chars += self.symbols
        
        if not chars:
            raise ValueError("At least one character type must be selected")
        
        # Generate password using cryptographically secure random
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password
    
    def check_strength(self, password):
        """Check password strength and return a score."""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Include lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Include uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Include numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Include symbols")
        
        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
        strength = strength_levels[min(score, 4)]
        
        return strength, feedback

def main():
    generator = PasswordGenerator()
    
    print("🔐 Password Generator")
    print("=" * 30)
    
    while True:
        try:
            # Get user preferences
            length = int(input("\nEnter password length (default 12): ") or "12")
            
            print("\nCharacter types to include:")
            use_lowercase = input("Lowercase letters? (Y/n): ").lower() != 'n'
            use_uppercase = input("Uppercase letters? (Y/n): ").lower() != 'n'
            use_digits = input("Numbers? (Y/n): ").lower() != 'n'
            use_symbols = input("Symbols? (Y/n): ").lower() != 'n'
            
            # Generate password
            password = generator.generate_password(
                length=length,
                use_lowercase=use_lowercase,
                use_uppercase=use_uppercase,
                use_digits=use_digits,
                use_symbols=use_symbols
            )
            
            # Show results
            print(f"\n✅ Generated Password: {password}")
            
            # Check strength
            strength, feedback = generator.check_strength(password)
            print(f"🛡️  Strength: {strength}")
            
            if feedback:
                print("💡 Suggestions:")
                for tip in feedback:
                    print(f"   • {tip}")
            
            # Ask if user wants another password
            if input("\nGenerate another password? (Y/n): ").lower() == 'n':
                break
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
    
    print("Thanks for using Password Generator!")

if __name__ == "__main__":
    main()