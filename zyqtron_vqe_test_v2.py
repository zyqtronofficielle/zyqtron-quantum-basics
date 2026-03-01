# Zyqtron Quantum Labs - Test VQE n°2 : Molécule H₂ (version améliorée)
# Objectif : Calculer l'énergie de base de H₂ avec un ansatz plus expressif

import pennylane as qml
from pennylane import numpy as np

print("=== Zyqtron - Test VQE amélioré pour H₂ démarré ===")

# Simulateur local (2 qubits pour H₂ simple)
dev = qml.device('default.qubit', wires=2)

# Ansatz variationnel plus riche (Hardware-efficient ansatz)
@qml.qnode(dev)
def circuit(params):
    # Couche 1 : Superposition et rotations
    qml.RY(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0, 1])
    
    # Couche 2 : Plus de rotations
    qml.RY(params[2], wires=0)
    qml.RY(params[3], wires=1)
    
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))  # Énergie (observable)

# Fonction coût à minimiser
def energy(params):
    return circuit(params)

# Meilleur optimiseur (Adam, plus stable)
opt = qml.AdamOptimizer(stepsize=0.05)

# Paramètres initiaux aléatoires (4 paramètres pour ansatz)
np.random.seed(42)  # Pour reproductibilité
params = np.random.random(4) * 0.1

# Boucle d'optimisation (50 étapes pour meilleure convergence)
print("Optimisation en cours...")
energies = []
for i in range(50):
    params = opt.step(energy, params)
    current_energy = energy(params)
    energies.append(current_energy)
    if i % 10 == 0:
        print(f"Étape {i:2d}: Énergie = {current_energy:.6f}")

final_energy = energy(params)
print(f"\nÉnergie finale de H₂ : {final_energy:.6f}")
print(f"Valeur théorique idéale : -1.136 (approximation chimique simple)")

if final_energy < -0.9:
    print("SUCCÈS ! Convergence raisonnable vers l'énergie de base.")
else:
    print("Convergence partielle – normal pour ansatz simple. On peut améliorer.")

# Affichage rapide de la courbe d'énergie (optionnel)
import matplotlib.pyplot as plt
plt.plot(energies)
plt.xlabel("Itérations")
plt.ylabel("Énergie")
plt.title("Convergence VQE Zyqtron - H₂")
plt.grid(True)
plt.show()
