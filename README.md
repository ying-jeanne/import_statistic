# import_statistic

1. List all direct dependency of your project 
go list -m -f '{{if not .Indirect}}{{.Path}}{{end}}' all > dependencies.txt

2. Run script to count number of import in your project for each of the dependent library
3. Analyse each of the potential case manually
