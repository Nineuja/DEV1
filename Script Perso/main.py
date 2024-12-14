import os
import csv
import sys
from typing import List, Optional


def get_base_path() -> str:
    """
    Obtient le chemin de base du script de manière compatible multi-plateforme.

    Returns:
        str: Chemin absolu du répertoire contenant le script
    """
    # Utiliser sys.executable pour les scripts empaquetés, sinon utiliser __file__
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


def create_directory(directory: str) -> None:
    """
    Crée un répertoire de manière sécurisée et compatible.

    Args:
        directory (str): Chemin du répertoire à créer
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Erreur lors de la création du répertoire {directory}: {e}")
        sys.exit(1)


def validate_csv_file(file_path: str) -> bool:
    """
    Vérifie la structure du fichier CSV.

    Args:
        file_path (str): Chemin du fichier CSV

    Returns:
        bool: True si le fichier a le bon format, False sinon
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader)
            return len(first_row) == 4
    except Exception as e:
        print(f"Erreur lors de la validation du fichier {file_path}: {e}")
        return False


def merge_csv_files(input_folder: str) -> Optional[List[List[str]]]:
    """
    Fusionne les fichiers CSV du dossier d'entrée.

    Args:
        input_folder (str): Chemin du dossier contenant les fichiers CSV

    Returns:
        Optional[List[List[str]]]: Liste des données fusionnées ou None en cas d'erreur
    """
    merged_data: List[List[str]] = []

    # Vérifier l'existence du dossier d'entrée
    if not os.path.exists(input_folder):
        print(f"Erreur : Le dossier {input_folder} n'existe pas.")
        return None

    # Parcourir tous les fichiers CSV du dossier
    try:
        for filename in os.listdir(input_folder):
            # Utiliser os.path.join pour la compatibilité des chemins
            file_path = os.path.join(input_folder, filename)

            # Vérifier que c'est bien un fichier CSV
            if not filename.lower().endswith('.csv'):
                continue

            if not validate_csv_file(file_path):
                print(f"Fichier {filename} ignoré - structure invalide")
                continue

            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                merged_data.extend(list(reader))

    except Exception as e:
        print(f"Erreur lors de la lecture des fichiers CSV: {e}")
        return None

    return merged_data


def write_merged_csv(data: List[List[str]], output_folder: str) -> None:
    """
    Écrit les données fusionnées dans un fichier CSV.

    Args:
        data (List[List[str]]): Données à écrire
        output_folder (str): Dossier de destination
    """
    # Créer le chemin complet du fichier de sortie
    output_file = os.path.join(output_folder, 'produits_fusionnes.csv')

    # Supprimer le fichier existant si nécessaire
    if os.path.exists(output_file):
        os.remove(output_file)

    # Écrire le fichier CSV
    if data:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        print(f"Fichier fusionné créé : {output_file}")
    else:
        print("Aucune donnée à écrire.")


def main():
    """
    Fonction principale pour exécuter le script de fusion CSV.
    """
    # Obtenir le chemin de base du script
    base_dir = get_base_path()

    # Construire les chemins des dossiers de manière compatible
    input_folder = os.path.join(base_dir, 'CSV-init')
    output_folder = os.path.join(base_dir, 'CSV-core')

    # Créer les dossiers si nécessaire
    create_directory(input_folder)
    create_directory(output_folder)

    # Fusionner les fichiers CSV
    merged_data = merge_csv_files(input_folder)

    if merged_data is None:
        print("Erreur lors de la fusion des fichiers CSV.")
        sys.exit(1)

    # Afficher les données en console
    print("\n--- Données fusionnées ---")
    for row in merged_data:
        print(row)

    # Écrire le fichier CSV fusionné
    write_merged_csv(merged_data, output_folder)


if __name__ == "__main__":
    main()