import os
import subprocess

def install_dependencies():
    # Python dependencies
    if os.path.exists("requirements.txt"):
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Node.js dependencies
    if os.path.exists("package.json"):
        subprocess.run(["npm", "install"])

    # Ruby dependencies (Gemfile)
    if os.path.exists("Gemfile"):
        subprocess.run(["bundle", "install"])

    # PHP dependencies (composer.json)
    if os.path.exists("composer.json"):
        subprocess.run(["composer", "install"])

    # Java dependencies (pom.xml for Maven)
    if os.path.exists("pom.xml"):
        subprocess.run(["mvn", "install"])

    print("Dependency installation completed.")

if __name__ == "__main__":
    install_dependencies()
