import tkinter as tk
from tkinter import messagebox

def valid_dna(seq):
    return all(base in "ATGC" for base in seq.upper())

def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return round((g + c) / len(seq) * 100, 2)

def at_content(seq):
    a = seq.count('A')
    t = seq.count('T')
    return round((a + t) / len(seq) * 100, 2)

def transcribe_dna(seq):
    return seq.replace('T', 'U')

def translate_dna(seq):
    codon_table = {
        'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
        'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
        'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
        'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
        'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
        'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
        'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
        'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
        'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
        'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
        'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
        'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
        'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
        'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
        'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
        'TGC':'C','TGT':'C','TGA':'_','TGG':'W'
    }
    protein = ""
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        amino_acid = codon_table.get(codon, 'X')
        if amino_acid == '_':
            break
        protein += amino_acid
    return protein

def analyze_sequence():
    sequence = entry.get("1.0", tk.END).strip().upper()

    if not valid_dna(sequence):
        messagebox.showerror("Invalid Input", "Please enter a valid DNA sequence (A, T, G, C only).")
        return

    gc = gc_content(sequence)
    at = at_content(sequence)
    rna = transcribe_dna(sequence)
    protein = translate_dna(sequence)

    output_text.set(f"""--- DNA Analysis Result ---
Length: {len(sequence)}
GC Content: {gc}%
AT Content: {at}%
RNA (Transcribed): {rna}
Protein (Translated): {protein}
""")

root = tk.Tk()
root.title("DNA Sequence Analyzer")
root.geometry("600x400")

tk.Label(root, text="Enter DNA Sequence:", font=("Arial", 12)).pack(pady=10)

entry = tk.Text(root, height=5, width=60)
entry.pack()

tk.Button(root, text="Analyze", command=analyze_sequence, font=("Arial", 12)).pack(pady=10)

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, justify="left", font=("Courier", 10), bg="white", anchor="w", width=80, height=10, relief="sunken")
output_label.pack(padx=10, pady=10, fill="both")

root.mainloop()
