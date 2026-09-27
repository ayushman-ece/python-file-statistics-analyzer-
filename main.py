from file_analyzer import FileAnalyzer


folder = input("Enter folder path: ").strip()

analyzer = FileAnalyzer(folder)

analyzer.analyze()