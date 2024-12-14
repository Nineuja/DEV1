import os
import csv
import sys
from typing import List, Optional

class CSVMerger:
    """
    Classe de fusion de fichiers CSV multi-plateforme.

    Cette classe gère la lecture, la validation et la fusion de fichiers CSV
    provenant d'un dossier source vers un dossier de destination.
    """

    def __init__(self, input_folder: str = 'CSV-init', output_folder: str = 'CSV-core'):
        """
        Initialise le fusionneur de CSV.

        Args:
            input_folder (str): Nom du dossier source des CSV
            output_folder (str): Nom du dossier de destination
        """
        self.base_dir = self._get_base_path()
        self.input_folder = os.path.join(self.base_dir, input_folder)
        self.output_folder = os.path.join(self.base_dir, output_folder)

    @staticmethod
    def _get_base_path() -> str:
        """
        Obtient le chemin de base du script de manière compatible multi-plateforme.

        Returns:
            str: Chemin absolu du répertoire contenant le script
        """
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(os.path.abspath(__file__))

    def _create_directories(self) -> None:
        """
        Crée les répertoires d'entrée et de sortie de manière sécurisée.
        """
        try:
            os.makedirs(self.input_folder, exist_ok=True)
            os.makedirs(self.output_folder, exist_ok=True)
        except OSError as e:
            print(f"Erreur lors de la création des répertoires : {e}")
            sys.exit(1)

    @staticmethod
    def _validate_csv_file(file_path: str) -> bool:
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

    def merge_csv_files(self) -> Optional[List[List[str]]]:
        """
        Fusionne les fichiers CSV du dossier d'entrée.

        Returns:
            Optional[List[List[str]]]: Liste des données fusionnées ou None en cas d'erreur
        """
        merged_data: List[List[str]] = []

        # Vérifier l'existence du dossier d'entrée
        if not os.path.exists(self.input_folder):
            print(f"Erreur : Le dossier {self.input_folder} n'existe pas.")
            return None

        # Parcourir tous les fichiers CSV du dossier
        try:
            for filename in os.listdir(self.input_folder):
                # Utiliser os.path.join pour la compatibilité des chemins
                file_path = os.path.join(self.input_folder, filename)

                # Vérifier que c'est bien un fichier CSV
                if not filename.lower().endswith('.csv'):
                    continue

                if not self._validate_csv_file(file_path):
                    print(f"Fichier {filename} ignoré - structure invalide")
                    continue

                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    merged_data.extend(list(reader))
        except Exception as e:
            print(f"Erreur lors de la lecture des fichiers CSV: {e}")
            return None
        return merged_data

    def write_merged_csv(self, data: List[List[str]], output_filename: str = 'produits_fusionnes.csv') -> None:
        """
        Écrit les données fusionnées dans un fichier CSV.

        Args:
            data (List[List[str]]): Données à écrire
            output_filename (str): Nom du fichier de sortie
        """
        # Créer le chemin complet du fichier de sortie
        output_file = os.path.join(self.output_folder, output_filename)

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

    def run(self) -> None:
        """
        Méthode principale exécutant la fusion des CSV.
        """
        # Créer les dossiers si nécessaire
        self._create_directories()

        # Fusionner les fichiers CSV
        merged_data = self.merge_csv_files()

        if merged_data is None:
            print("Erreur lors de la fusion des fichiers CSV.")
            sys.exit(1)

        # Afficher les données en console
        print("\n--- Données fusionnées ---")
        for row in merged_data:
            print(row)

        # Écrire le fichier CSV fusionné
        self.write_merged_csv(merged_data)
