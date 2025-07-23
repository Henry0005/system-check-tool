import subprocess
import platform

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        return result.stdout if result.returncode == 0 else f"Erro: {result.stderr}"
    except Exception as e:
        return f"Erro ao executar '{cmd}': {str(e)}"

def get_windows_info():
    return {
        "Informações do Sistema": run_command("systeminfo"),
        "CPU": run_command("wmic cpu get caption"),
        "Memória": run_command("wmic memorychip get capacity"),
        "Disco": run_command("wmic logicaldisk get size,freespace,caption,filesystem")
    }

def get_linux_info():
    return {
        "Informações do Sistema": run_command("uname -a"),
        "CPU": run_command("lscpu"),
        "Memória": run_command("free -h"),
        "Disco": run_command("df -h")
    }

def get_system_info():
    os_type = platform.system()
    if os_type == "Windows":
        return get_windows_info()
    elif os_type == "Linux":
        return get_linux_info()
    else:
        return {"Erro": f"SO '{os_type}' não suportado."}

def print_info(info):
    for key, value in info.items():
        print(f"{key}:\n{value.strip()}\n{'-' * 50}")

def main():
    print("🔍 Coletando informações do sistema...\n")
    info = get_system_info()
    print_info(info)

if __name__ == "__main__":
    main()
