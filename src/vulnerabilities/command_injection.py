"""
This module contains examples of command injection vulnerabilities.
Command injection occurs when user input is directly incorporated into system commands without proper sanitization.
"""

import os
import subprocess
import shlex
from typing import List, Dict, Any, Optional


# ISSUE: Basic command injection vulnerability with os.system
def ping_host_vulnerable(host: str) -> int:
    """
    Ping a host to check if it's reachable.
    Contains a command injection vulnerability due to unsanitized input.
    
    Example exploit: host = "google.com && rm -rf /important_files"
    """
    # Vulnerable: Unsanitized input passed to os.system
    command = f"ping -c 4 {host}"
    return os.system(command)


# ISSUE: Command injection with string concatenation in subprocess.call
def check_dns_vulnerable(domain: str) -> List[str]:
    """
    Check DNS records for a domain.
    Contains a command injection vulnerability due to string concatenation.
    
    Example exploit: domain = "example.com; cat /etc/passwd"
    """
    # Vulnerable: String concatenation with unsanitized input
    command = "nslookup " + domain
    
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


# ISSUE: Command injection in subprocess.Popen with shell=True
def get_file_info_vulnerable(filename: str) -> Dict[str, Any]:
    """
    Get information about a file.
    Contains a command injection vulnerability due to shell=True.
    
    Example exploit: filename = "file.txt; rm -rf /"
    """
    # Vulnerable: shell=True with unsanitized input
    command = f"ls -la {filename}"
    
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"Error: {stderr}")
            return {}
        
        return {
            "output": stdout,
            "return_code": process.returncode
        }
    except Exception as e:
        print(f"Error: {e}")
        return {}


# ISSUE: Command injection with multiple commands
def backup_file_vulnerable(filename: str, backup_dir: str) -> bool:
    """
    Backup a file to a specified directory.
    Contains a command injection vulnerability with multiple unsanitized inputs.
    
    Example exploit: filename = "file.txt; rm -rf /"
    """
    # Vulnerable: Multiple unsanitized inputs
    command = f"cp {filename} {backup_dir}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


# ISSUE: Command injection in a more complex command
def search_logs_vulnerable(keyword: str, log_file: str) -> List[str]:
    """
    Search for a keyword in log files.
    Contains a command injection vulnerability in a complex command.
    
    Example exploit: keyword = "error\" | cat /etc/passwd #"
    """
    # Vulnerable: Complex command with unsanitized inputs
    command = f'grep "{keyword}" {log_file} | sort | uniq -c'
    
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


# ISSUE: Command injection with template strings
def generate_report_vulnerable(report_name: str, output_format: str) -> str:
    """
    Generate a report in the specified format.
    Contains a command injection vulnerability with template strings.
    
    Example exploit: output_format = "pdf; rm -rf /"
    """
    # Vulnerable: Template string with unsanitized input
    command = f"report-tool generate --name {report_name} --format {output_format}"
    
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return f"Report generated successfully: {output}"
    except subprocess.CalledProcessError as e:
        return f"Error generating report: {e}"


# ISSUE: Command injection with user-controlled file paths
def extract_archive_vulnerable(archive_path: str, extract_path: str) -> bool:
    """
    Extract an archive to the specified path.
    Contains a command injection vulnerability with user-controlled file paths.
    
    Example exploit: archive_path = "archive.tar.gz; rm -rf /"
    """
    # Vulnerable: User-controlled file paths
    command = f"tar -xzf {archive_path} -C {extract_path}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


# ISSUE: Command injection with environment variables
def run_with_env_vulnerable(command: str, env_vars: Dict[str, str]) -> str:
    """
    Run a command with specified environment variables.
    Contains a command injection vulnerability with environment variables.
    
    Example exploit: command = "ls; rm -rf /"
    """
    # Vulnerable: Unsanitized command
    env_str = " ".join([f"{k}={v}" for k, v in env_vars.items()])
    full_command = f"{env_str} {command}"
    
    try:
        output = subprocess.check_output(full_command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


# ISSUE: Indirect command injection through eval
def calculate_expression_vulnerable(expression: str) -> float:
    """
    Calculate a mathematical expression.
    Contains an indirect command injection vulnerability through eval.
    
    Example exploit: expression = "__import__('os').system('rm -rf /')"
    """
    # Vulnerable: Using eval on unsanitized input
    try:
        result = eval(expression)
        return float(result)
    except Exception as e:
        print(f"Error: {e}")
        return 0.0


# BETTER ALTERNATIVE: Using subprocess with argument lists instead of shell=True

def ping_host_safe(host: str) -> int:
    """
    Ping a host to check if it's reachable, safely.
    """
    try:
        # Safe: Using argument list instead of shell=True
        result = subprocess.run(
            ["ping", "-c", "4", host],
            capture_output=True,
            text=True,
            check=False
        )
        return result.returncode
    except Exception as e:
        print(f"Error: {e}")
        return -1


def check_dns_safe(domain: str) -> List[str]:
    """
    Check DNS records for a domain, safely.
    """
    try:
        # Safe: Using argument list instead of shell=True
        result = subprocess.run(
            ["nslookup", domain],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout.splitlines()
    except Exception as e:
        print(f"Error: {e}")
        return []


# BETTER ALTERNATIVE: Using shlex.quote to escape shell arguments

def get_file_info_safer_but_still_risky(filename: str) -> Dict[str, Any]:
    """
    Get information about a file, with escaped arguments.
    This is safer but still uses shell=True, which is risky.
    """
    # Safer but still risky: Escaping arguments but still using shell=True
    escaped_filename = shlex.quote(filename)
    command = f"ls -la {escaped_filename}"
    
    try:
        process = subprocess.Popen(
            command,
            shell=True,  # Still risky
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"Error: {stderr}")
            return {}
        
        return {
            "output": stdout,
            "return_code": process.returncode
        }
    except Exception as e:
        print(f"Error: {e}")
        return {}


def get_file_info_safe(filename: str) -> Dict[str, Any]:
    """
    Get information about a file, safely.
    """
    try:
        # Safe: Using argument list instead of shell=True
        process = subprocess.run(
            ["ls", "-la", filename],
            capture_output=True,
            text=True,
            check=False
        )
        
        return {
            "output": process.stdout,
            "return_code": process.returncode,
            "error": process.stderr if process.returncode != 0 else None
        }
    except Exception as e:
        print(f"Error: {e}")
        return {}


# BETTER ALTERNATIVE: Input validation and whitelisting

def generate_report_safe(report_name: str, output_format: str) -> str:
    """
    Generate a report in the specified format, safely.
    """
    # Validate output format against a whitelist
    allowed_formats = ["pdf", "html", "csv", "json"]
    
    if output_format not in allowed_formats:
        return f"Error: Invalid output format '{output_format}'. Allowed formats: {', '.join(allowed_formats)}"
    
    try:
        # Safe: Using argument list with validated input
        result = subprocess.run(
            ["report-tool", "generate", "--name", report_name, "--format", output_format],
            capture_output=True,
            text=True,
            check=True
        )
        return f"Report generated successfully: {result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error generating report: {e}"


# BETTER ALTERNATIVE: Using built-in Python functions instead of external commands

def extract_archive_safe(archive_path: str, extract_path: str) -> bool:
    """
    Extract an archive to the specified path, safely using Python's tarfile module.
    """
    import tarfile
    
    try:
        # Validate that the paths exist and are within allowed directories
        if not os.path.exists(archive_path):
            print(f"Error: Archive file does not exist: {archive_path}")
            return False
        
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
        
        # Safe: Using Python's built-in tarfile module
        with tarfile.open(archive_path, "r:gz") as tar:
            # Additional security: Check for path traversal attacks
            for member in tar.getmembers():
                if member.name.startswith("/") or ".." in member.name:
                    print(f"Security warning: Skipping potentially malicious path: {member.name}")
                    continue
                tar.extract(member, extract_path)
        
        return True
    except Exception as e:
        print(f"Error extracting archive: {e}")
        return False


# BETTER ALTERNATIVE: Safe mathematical expression evaluation

def calculate_expression_safe(expression: str) -> float:
    """
    Calculate a mathematical expression safely using ast.literal_eval.
    """
    import ast
    import operator
    
    # Define allowed operators
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }
    
    def eval_expr(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](eval_expr(node.operand))
        else:
            raise TypeError(f"Unsupported type: {node}")
    
    try:
        # Parse the expression
        node = ast.parse(expression, mode='eval').body
        # Evaluate it safely
        return eval_expr(node)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return 0.0