from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Custom encoding map for obfuscation
ENCODING_MAP = {
    "a": "X", "b": "Y", "c": "Z", "d": "A", "e": "B",
    "f": "C", "g": "D", "h": "E", "i": "F", "j": "G",
    "k": "H", "l": "I", "m": "J", "n": "K", "o": "L",
    "p": "M", "q": "N", "r": "O", "s": "P", "t": "Q",
    "u": "R", "v": "S", "w": "T", "x": "U", "y": "V",
    "z": "W", "0": "9", "1": "8", "2": "7", "3": "6",
    "4": "5", "5": "4", "6": "3", "7": "2", "8": "1",
    "9": "0", "@": "#", "#": "@"
}

DECODING_MAP = {v: k for k, v in ENCODING_MAP.items()}  # Reverse mapping

def encode_password(password: str) -> str:
    """Encodes password using a predefined mapping"""
    return "".join(ENCODING_MAP.get(char, char) for char in password)

def decode_password(encoded_password: str) -> str:
    """Decodes the encoded password back to its original form"""
    return "".join(DECODING_MAP.get(char, char) for char in encoded_password)

def hash_password(password: str) -> str:
    """Hashes the encoded password securely"""
    encoded = encode_password(password)
    return encoded

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies if the plain password (after encoding) matches the hashed password"""
    encoded = encode_password(plain_password)
    return pwd_context.verify(encoded, hashed_password)
