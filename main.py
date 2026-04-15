import subprocess # Para executar comandos no terminal.
import os # Apenas para limpar o terminal, já que subprocess não limpa corretamente em algumas IDEs.
 

# Dicionário de apps para futuras atualizações
apps = {
    "VSCode": "Microsoft.VisualStudioCode", 
    "IntelliJ": "JetBrains.IntelliJIDEA.Community", 
    "WebStorm": "JetBrains.WebStorm ", 
    "PyCharm": "JetBrains.PyCharm", 
    "Git": "Git.Git", 
    "GitHub": "GitHub.GitHubDesktop", 
    "GitLab": "GLab.GLab", 
    "Docker": "Docker.DockerDesktop", 
    "Postman": "Postman.Postman", 
    "Postman (ARM64)": "Postman.Postman.arm64",
    "Insomnia": "Insomnia.Insomnia", 
    "DBeaver": "DBeaver.DBeaver.Community", 
    "TablePlus": "TablePlus.TablePlus",
    "Notion": "Notion.Notion", 
    "Todoist": "Doist.Todoist", 
    "Obsidian": "Obsidian.Obsidian", 
    "Slack": "SlackTechnologies.Slack", 
    "Discord": "Discord.Discord", 
    "Trello (MS Store)": "9NBLGGH4XXVW", 
    "Linear": "LinearOrbit.Linear",  
    "Figma": "Figma.Figma", 
    "Canva": "Canva.Canva"
}

# Lista das apps em ordem alfabética
apps_abc = sorted(apps)

# Dicionário de apps em UPPER case para cuidado de escrita
apps_upper = {app.upper(): apps[app] for app in sorted(apps)}




# Execussão do código no terminal
def escolha(esc):
    try:
        resultado = subprocess.run(["winget", "update", apps_upper[esc]], capture_output=True, text=True) # Captura o output e transforma de bytes para texto
        print(resultado.stdout.splitlines()[-1]) # Printa o resultado
    except ValueError:
        print("Nenhuma app encontrada. | no app found.")
            

while True:
    print("========================================================================================================================================")
    print("Bem vindo ao instalador de apps | Welcome to app installer\n" \
          "Escolhe das apps indicadas a baixo as que gostarias de instalar. | Choose from the apps listed below the ones you would like to install.\n")
    print("========================================================================================================================================")
    for i in range(0, len(apps_abc) - 3, 1):
        if i & 3 == 0:
            print("\n")
        print(" | " + apps_abc[i] + (" " * (len(max(apps_abc, key=len)) - len(apps_abc[i]))), end="")
        
    print("\n\n\n========================================================================================================================================")
    escolha(input("\nInsira o nome | Enter the name: ").strip().upper())
    print("========================================================================================================================================")
    mais = input("Deseja instalar mais algo? [S/N]| Do you want to install something else? [Y/N]: ").upper()

    if mais in ["YES", "Y", "SIM", "S"]:
        os.system('cls')
        continue
    elif mais in ["NO", "N", "NÃO", "NAO"]:
        break
    else:
        while mais not in ["YES", "Y", "SIM", "S", "NO", "N", "NÃO", "NAO"]:
            mais = input("\n\nOpção invalida, escolha denovo | Invalid option, choose again: ")