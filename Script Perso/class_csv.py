import os
import csv
import sys
from typing import List, Optional
from datetime import datetime

class InputError(Exception):
    """Exception personnalisée pour les erreurs d'input utilisateur."""
    pass


class CSVMerger:
    """
    Classe de fusion et de tri avancée de fichiers CSV multi-plateforme.

    Gère la lecture, la validation, la fusion et le tri de fichiers CSV
    avec des fonctionnalités interactives étendues.
    """

    def __init__(self,
                 input_folder: str = 'CSV-init',
                 output_folder: str = 'CSV-core',
                 sort_folder: str = 'CSV-sort'):
        """
        Initialise le fusionneur de CSV avec des dossiers personnalisés.

        Args:
            input_folder (str): Nom du dossier source des CSV
            output_folder (str): Nom du dossier de destination principale
            sort_folder (str): Nom du dossier pour les CSV triés
        """
        self.base_dir = self._get_base_path()
        self.input_folder = os.path.join(self.base_dir, input_folder)
        self.output_folder = os.path.join(self.base_dir, output_folder)
        self.sort_folder = os.path.join(self.base_dir, sort_folder)

        # Définition des colonnes avec leurs index
        self.columns = {
            'nom': 0,
            'quantité': 1,
            'prix': 2,
            'catégorie': 3
        }

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
        Crée les répertoires d'entrée, de sortie et de tri de manière sécurisée.
        """
        try:
            os.makedirs(self.input_folder, exist_ok=True)
            os.makedirs(self.output_folder, exist_ok=True)
            os.makedirs(self.sort_folder, exist_ok=True)
        except OSError as e:
            print(f"Erreur lors de la création des répertoires : {e}")
            sys.exit(1)

    def _validate_csv_file(self, file_path: str) -> bool:
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
                    # Ignorer l'en-tête du premier fichier
                    next(reader, None)
                    for row in reader:
                        merged_data.append(row)

        except Exception as e:
            print(f"Erreur lors de la lecture des fichiers CSV: {e}")
            return None
        return merged_data

    def write_csv(self, data: List[List[str]], output_path: str) -> None:
        """
        Écrit les données dans un fichier CSV.

        Args:
            data (List[List[str]]): Données à écrire
            output_path (str): Chemin complet du fichier de sortie
        """
        # Supprimer le fichier existant si nécessaire
        if os.path.exists(output_path):
            os.remove(output_path)

        # Écrire le fichier CSV
        if data:
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # Réajouter l'en-tête
                writer.writerow(['Nom', 'Quantité', 'Prix', 'Catégorie'])
                writer.writerows(data)

            print(f"Fichier créé : {output_path}")
        else:
            print("Aucune donnée à écrire.")

    def _get_validated_input(self,
                             prompt: str,
                             valid_options: Optional[List[str]] = None,
                             error_message: Optional[str] = None) -> str:
        """
        Obtient un input validé de l'utilisateur.

        Args:
            prompt (str): Message à afficher pour l'input
            valid_options (Optional[List[str]]): Liste des options valides
            error_message (Optional[str]): Message d'erreur personnalisé

        Returns:
            str: Input validé de l'utilisateur
        """
        while True:
            try:
                user_input = input(prompt).lower().strip()

                # Si aucune option spécifiée, retourner l'input
                if valid_options is None:
                    return user_input

                # Vérifier si l'input est dans les options valides
                if user_input in valid_options:
                    return user_input

                # Lancer une exception si l'input n'est pas valide
                raise InputError(error_message or "Option invalide. Veuillez réessayer.")

            except InputError as e:
                print(f"\n{e}")
            except Exception as e:
                print(f"\nUne erreur inattendue s'est produite : {e}")

    def advanced_sort_method(self, data: List[List[str]]) -> Optional[List[List[str]]]:
        """
        Méthode de tri avancée avec sélection de colonne par nom ou catégorie.

        Args:
            data (List[List[str]]): Données à trier

        Returns:
            Optional[List[List[str]]]: Données triées ou None
        """
        # Créer une copie des données pour ne pas modifier l'original
        current_data = data.copy()

        while True:
            # Afficher les options de colonnes
            print("\nChoisissez la colonne à trier :")
            for i, col in enumerate(self.columns.keys(), 1):
                print(f"{i}. {col.capitalize()}")
            print("5. Terminer le tri et sauvegarder")
            print("6. Retour au menu principal")

            # Obtenir le choix de la colonne avec validation
            try:
                choix_colonne = self._get_validated_input(
                    "Entrez votre choix (1-6) : ",
                    ['1', '2', '3', '4', '5', '6'],
                    "Veuillez entrer un nombre entre 1 et 6."
                )

                # Option de retour au menu principal
                if choix_colonne == '6':
                    return None

                # Option de sauvegarde finale
                if choix_colonne == '5':
                    # Demander un nom de fichier pour la sauvegarde
                    save_choice = self._get_validated_input(
                        "Voulez-vous enregistrer ces données triées ? (o/n) : ",
                        ['o', 'n'],
                        "Veuillez répondre par 'o' ou 'n'."
                    )

                    if save_choice == 'o':
                        # Validation du nom de fichier
                        while True:
                            filename = input("Entrez le nom du fichier CSV (sans extension) : ").strip()
                            if filename:
                                output_path = os.path.join(self.sort_folder, f"{filename}.csv")
                                self.write_csv(current_data, output_path)
                                break
                            print("Le nom de fichier ne peut pas être vide.")
                    return current_data

                # Convertir le choix en nom de colonne
                column_name = list(self.columns.keys())[int(choix_colonne) - 1]
                column_index = self.columns[column_name]

                # Choix de l'ordre de tri avec validation
                ordre_options = ['1', '2']
                print("\nChoisissez l'ordre de tri :")
                print("1. Ascendant")
                print("2. Descendant")

                choix_ordre = self._get_validated_input(
                    "Entrez votre choix d'ordre (1-2) : ",
                    ordre_options,
                    "Veuillez entrer 1 pour ascendant ou 2 pour descendant."
                )
                reverse = choix_ordre == '2'

                # Trier les données
                if column_index in [1, 2]:  # Colonnes numériques
                    current_data = sorted(current_data, key=lambda x: float(x[column_index]), reverse=reverse)
                else:  # Colonnes textuelles
                    current_data = sorted(current_data, key=lambda x: x[column_index], reverse=reverse)

                # Afficher les données triées
                print("\n--- Données triées ---")
                for row in current_data:
                    print(row)

            except ValueError as e:
                print(f"\nErreur de conversion : {e}")
            except Exception as e:
                print(f"\nUne erreur inattendue s'est produite : {e}")

    def generate_csv_report(self, data: List[List[str]]) -> None:
        """
        Génère un rapport récapitulatif des données CSV et l'exporte dans un fichier txt.

        Args:
            data (List[List[str]]): Données à analyser pour le rapport
        """
        # Créer le dossier de récapitulatif s'il n'existe pas
        recap_folder = os.path.join(self.base_dir, 'CSV-recap')
        os.makedirs(recap_folder, exist_ok=True)

        # Générer un nom de fichier avec date et heure
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recap_{current_time}.txt"
        filepath = os.path.join(recap_folder, filename)

        # Calculs pour le rapport
        try:
            # Conversion des données numériques
            quantities = [float(row[1]) for row in data]
            prices = [float(row[2]) for row in data]

            # Statistiques générales
            total_items = len(data)
            total_quantity = sum(quantities)
            total_value = sum(price * quantity for price, quantity in zip(prices, quantities))

            # Analyse par catégorie
            categories = {}
            for row in data:
                category = row[3]
                qty = float(row[1])
                value = float(row[2]) * qty

                if category not in categories:
                    categories[category] = {'quantity': 0, 'total_value': 0, 'items': []}

                categories[category]['quantity'] += qty
                categories[category]['total_value'] += value
                categories[category]['items'].append(row[0])

            # Rédaction du rapport
            with open(filepath, 'w', encoding='utf-8') as report_file:
                report_file.write("=== RAPPORT RÉCAPITULATIF DES DONNÉES CSV ===\n")
                report_file.write(f"Date et heure : {current_time}\n\n")

                report_file.write("--- STATISTIQUES GÉNÉRALES ---\n")
                report_file.write(f"Nombre total d'articles : {total_items}\n")
                report_file.write(f"Quantité totale : {total_quantity:.2f}\n")
                report_file.write(f"Valeur totale : {total_value:.2f} €\n\n")

                report_file.write("--- ANALYSE PAR CATÉGORIE ---\n")
                for category, data in sorted(categories.items(), key=lambda x: x[1]['total_value'], reverse=True):
                    report_file.write(f"\n{category.upper()}:\n")
                    report_file.write(f"  Quantité totale : {data['quantity']:.2f}\n")
                    report_file.write(f"  Valeur totale : {data['total_value']:.2f} €\n")
                    report_file.write(f"  Nombre d'articles : {len(data['items'])}\n")
                    report_file.write("  Articles : " + ", ".join(data['items']) + "\n")

            print(f"Rapport généré : {filepath}")

        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")

    def run(self) -> None:
        """
        Méthode principale exécutant la fusion des CSV et interaction utilisateur.
        """
        # Les étapes précédentes restent identiques
        # Créer les dossiers
        try:
            os.makedirs(self.input_folder, exist_ok=True)
            os.makedirs(self.output_folder, exist_ok=True)
            os.makedirs(self.sort_folder, exist_ok=True)
        except OSError as e:
            print(f"Erreur lors de la création des répertoires : {e}")
            sys.exit(1)

        # Fusionner les fichiers CSV
        merged_data = self.merge_csv_files()

        if merged_data is None:
            print("Erreur lors de la fusion des fichiers CSV.")
            sys.exit(1)

        # Écriture et affichage des données
        merged_output_path = os.path.join(self.output_folder, 'produits_fusionnes.csv')
        self.write_csv(merged_data, merged_output_path)

        print("\n--- Données fusionnées ---")
        for row in merged_data:
            print(row)

        # Boucle principale du menu
        while True:
            # Menu principal avec validation
            print("\nQue voulez-vous faire ?")
            print("1. Trier les données")
            print("2. Générer un rapport récapitulatif")
            print("3. Quitter")

            try:
                choix_principal = self._get_validated_input(
                    "Entrez votre choix (1-3) : ",
                    ['1', '2', '3'],
                    "Veuillez entrer 1 pour trier, 2 pour générer un rapport ou 3 pour quitter."
                )

                if choix_principal == '3':
                    print("Fin du programme.")
                    break

                if choix_principal == '1':
                    # Appeler la méthode de tri avancée
                    sorted_data = self.advanced_sort_method(merged_data)

                    if sorted_data:
                        # Mettre à jour les données fusionnées avec les données triées
                        merged_data = sorted_data

                if choix_principal == '2':
                    # Générer un rapport récapitulatif
                    self.generate_csv_report(merged_data)

            except Exception as e:
                print(f"Une erreur s'est produite : {e}")
