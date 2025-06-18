import argparse
import logging
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up the argument parser for the command-line interface.
    """
    parser = argparse.ArgumentParser(description='Smart Contract Static Analyzer for Cryptographic Vulnerabilities')
    parser.add_argument('contract_code', help='Smart contract bytecode or source code file path')
    parser.add_argument('--output', '-o', help='Output file to save analysis results', default='analysis_report.txt')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    return parser

def analyze_contract(contract_code, output_file):
    """
    Performs static analysis of the smart contract code.

    Args:
        contract_code (str): The smart contract bytecode or source code.
        output_file (str): The file to save the analysis results.
    """
    try:
        logging.info("Starting smart contract analysis...")

        # Basic checks (replace with more sophisticated analysis)
        if "tx.origin" in contract_code:
            log_warning("Potential tx.origin usage detected. This can be vulnerable to phishing attacks.", output_file)
        if "block.timestamp" in contract_code:
            log_warning("Potential timestamp dependence detected. This can be manipulated by miners.", output_file)
        if "unchecked" in contract_code:
            log_warning("Potential unchecked arithmetic operations detected. This could lead to overflow/underflow.", output_file)

        # Example: Check for potential weak random number generation
        if "keccak256(block.difficulty, block.timestamp)" in contract_code:
            log_warning("Weak random number generation detected. Avoid using block.difficulty and block.timestamp for randomness.", output_file)

        # Example: Check for outdated cryptography usage.  This is a very basic example and will need expansion.
        if "msg.data" in contract_code and "keccak256" in contract_code:
            log_info("Usage of keccak256 found. Ensure secure usage and appropriate padding.", output_file)

        # Placeholder for more advanced analysis: Control Flow Graph, Pattern Matching
        log_info("Performing basic vulnerability checks...", output_file)

        log_info("Analysis completed.", output_file)

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        log_error(f"Analysis failed due to error: {e}", output_file)

def log_info(message, output_file):
    """Logs an info message to the console and the output file."""
    logging.info(message)
    with open(output_file, "a") as f:
        f.write(f"[INFO] {message}\n")

def log_warning(message, output_file):
    """Logs a warning message to the console and the output file."""
    logging.warning(message)
    with open(output_file, "a") as f:
        f.write(f"[WARNING] {message}\n")

def log_error(message, output_file):
    """Logs an error message to the console and the output file."""
    logging.error(message)
    with open(output_file, "a") as f:
        f.write(f"[ERROR] {message}\n")

def validate_input(contract_code_path):
    """Validates the input file path."""
    try:
        with open(contract_code_path, 'r') as f:
            contract_code = f.read()
        return contract_code
    except FileNotFoundError:
        logging.error(f"File not found: {contract_code_path}")
        print(f"Error: File not found: {contract_code_path}")  # Print to stdout for immediate feedback
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        print(f"Error reading file: {e}")  # Print to stdout for immediate feedback
        sys.exit(1)

def main():
    """
    Main function to execute the smart contract static analyzer.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging to debug level

    contract_code = validate_input(args.contract_code)
    analyze_contract(contract_code, args.output)

# Example usage:
# python main.py contract.sol --output analysis.txt
# python main.py contract.bin -v

if __name__ == "__main__":
    main()