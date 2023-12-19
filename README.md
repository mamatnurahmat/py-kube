# py-kube

# docker build
docker build -t newrahmat/py-kube .

# windows
docker run -v %USERPROFILE%\.kube\config:/root/.kube/config -v %cd%:/app newrahmat/py-kube python main.py develop-saas > develop-saas.json

# linux
docker run -v "$HOME/.kube/config:/root/.kube/config" -v "$(pwd):/app" newrahmat/py-kube python main.py develop-saas > develop-saas.json
