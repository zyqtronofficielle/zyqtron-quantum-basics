# Zyqtron Quantum Labs - Test PennyLane n°1
# Ce code crée un circuit quantique très simple avec PennyLane
# Objectif : Montrer qu'on peut faire de la superposition et mesurer

import pennylane as qml
from pennylane import numpy as np

# On définit un "device" (simulateur local, 1 seul qubit)
dev = qml.device("default.qubit", wires=1)

# Fonction qui définit le circuit quantique
@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)  # Superposition : |0> → (|0> + |1>)/√2
    return qml.probs(wires=0)  # On mesure les probabilités

print("=== Zyqtron - Test PennyLane démarré ===")

# On exécute le circuit
result = circuit()

print("\nProbabilités mesurées après superposition :")
print(f"Probabilité d'être |0⟩ : {result[0]:.3f}")
print(f"Probabilité d'être |1⟩ : {result[1]:.3f}")

if abs(result[0] - 0.5) < 0.01 and abs(result[1] - 0.5) < 0.01:
    print("SUCCÈS ! Superposition parfaite (~50/50).")
else:
    print("Attention : résultat inattendu (vérifie l'installation).")
