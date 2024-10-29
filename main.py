import sys
from calculate import tokenize, prefix, postfix

def main():
    # Check command line arguments
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] != '-r'):
        print("USAGE: main.py [-r]")
        sys.exit(1)
        
    # Determine evaluation mode
    use_postfix = len(sys.argv) == 2
    
    # Process input lines
    while True:
        try:
            line = input()
            
            # Skip empty lines
            if not line.strip():
                continue
                
            # Tokenize input
            tokens = tokenize(line)
            
            # Evaluate expression
            result = postfix(tokens) if use_postfix else prefix(tokens)
            
            # Print result
            print(f"= {result}")
            
        except EOFError:
            break
        except RuntimeError as e:
            print(str(e))
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()