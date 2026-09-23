import argparse

from vigenere import decrypt, encrypt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text with the Vigenere cipher."
    )
    parser.add_argument("mode", choices=("encrypt", "decrypt"))
    parser.add_argument("text", help="Text to process")
    parser.add_argument("key", help="Key containing English letters only")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    try:
        result = encrypt(args.text, args.key) if args.mode == "encrypt" else decrypt(
            args.text, args.key
        )
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    print(result)


if __name__ == "__main__":
    main()

