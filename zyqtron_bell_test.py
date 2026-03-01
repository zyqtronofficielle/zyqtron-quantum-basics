# Zyqtron Quantum Labs - Premier test : État de Bell
# Ce code crée deux qubits intriqués (état de Bell)
# On utilise Qiskit et son simulateur local (Aer)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

print("--- Début du test Zyqtron : État de Bell ---")

# Création du circuit : 2 qubits + 2 bits classiques pour mesurer
qc = QuantumCircuit(2, 2)

# Étape 1 : Superposition sur le premier qubit (porte Hadamard)
qc.h(0)

# Étape 2 : Intrication avec le deuxième qubit (porte CNOT)
qc.cx(0, 1)

# Étape 3 : Mesure des deux qubits
qc.measure([0, 1], [0, 1])

print("\nCircuit créé :")
print(qc.draw())

# Lancement du simulateur local (sans bruit, parfait)
print("\nSimulation en cours...")
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)  # 1000 essais pour voir les stats

# Récupération des résultats
result = job.result()
counts = result.get_counts(qc)

print("\nRésultats après 1000 mesures :")
print(counts)

# Calcul de la fidélité (devrait être ~100 %)
total_valide = counts.get('00', 0) + counts.get('11', 0)
fidelite = (total_valide / 1000) * 100
print(f"Fidélité de l'intrication : {fidelite}%")

if fidelite >= 99:
    print("SUCCÈS ! L'intrication est parfaite (ou presque).")
else:
    print("Attention : Présence de bruit inattendu (normal sur simulateur ?).")

# Affichage graphique (histogramme)
plot_histogram(counts)
plt.show()
