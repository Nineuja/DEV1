from class_csv import CSVMerger


if __name__ == "__main__":
    import argparse
    
    # Create argument parser
    parser = argparse.ArgumentParser(description='CSV Merger with language support')
    parser.add_argument(
        '--lang', 
        type=str, 
        choices=['fr', 'en'], 
        default='fr',
        help='Choose language (fr: French, en: English)'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create CSVMerger instance and run with selected language
    merger = CSVMerger()
    merger.run(args.lang)