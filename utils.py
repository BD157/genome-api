def generate_kmers(sequence, k=6):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def process_sequence(sequence):
    # Simulated clustering logic
    return hash(sequence) % 5  # fake cluster ID for demo

def classify_sequence(sequence):
    return "BA.2" if "A" in sequence else "Other"
