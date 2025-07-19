import argparse 
import os

def get_cli_args(config_path:str):
    """
    Defines and parses CLI arguments using argparse.

    Args:
        default_config_path (str): Default config file path.

    Returns:
        argparse.Namespace: Parsed CLI arguments.
    """
    parser = argparse.ArgumentParser(
        prog='formatcode',
        description="FormatCode - A CLI tool to execute and format code outputs from multiple languages.",
        epilog="Example: formatcode --language Python --code-file test.py --format txt --input mymeta.json"
    )

    parser.add_argument(
        '--input',
        help="Path to custom metadata JSON file",
        default=config_path
    )
    parser.add_argument(
        '--language',
        help="Programming language to execute (Python, C, C++, Java)"
    )
    parser.add_argument(
        '--code-file',
        help="Path to source code file to be executed"
    )
    parser.add_argument(
        '--format',
        help="Output format for report generation (txt, latex, docx)"
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help="Run in interactive prompt mode"
    )
    parser.add_argument(
        '--version',
        action='version',
        version='formatcode 1.0.0',
        help="Display the version of the tool"
    )

    return parser.parse_args()
