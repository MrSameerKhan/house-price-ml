PHASE 0 — Clean Slate (Remove Old Jenkins Completely)
0.1 Stop and remove Jenkins container (if exists)
docker stop jenkins 2>/dev/null || true
docker rm jenkins 2>/dev/null || true

0.2 Remove Jenkins Docker image
docker rmi jenkins/jenkins:lts 2>/dev/null || true

0.3 Remove Jenkins volume (important)
docker volume rm jenkins_home 2>/dev/null || true


PHASE 1 — Ensure Docker Is Installed & Running
1.1 Install Docker Desktop (if not installed)
1.2 Start Docker Desktop
Open Docker Desktop
Wait until status = Running
1.3 Verify Docker
docker --version
docker info


PHASE 2 — Fresh Jenkins Installation (Correct Way)
We will install Jenkins with Docker access (this is critical).
2.1 Pull Jenkins image
docker pull jenkins/jenkins:lts
2.2 Run Jenkins (Correct Command — Read Carefully)
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
8080 → Jenkins UI
jenkins_home → persistent data
docker.sock → Jenkins can run Docker commands

PHASE 3 — Open Jenkins UI
Open browser:
http://localhost:8080

PHASE 4 — Initial Jenkins Setup
4.1 Get Admin Password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
4.2 Plugin Setup
Install suggested plugins
4.3 Create Admin User
4.4 Finish Setup
Start using Jenkins

PHASE 5 — Verify Jenkins Health
5.1 Check container
docker ps
Expected: jenkins   jenkins/jenkins:lts   Up   8080->8080
5.2 Verify Docker access from Jenkins (Important)
docker exec -it jenkins docker ps
If this works → Jenkins can control Docker



------------------------------------------ 
Two correct ways to solve this (important)
Option A — Recommended for learning (BEST for you)
Use Jenkins with Docker pre-installed
Option B — Manually install Docker CLI inside Jenkins
(more complex, less clean)
We will do Option A.

Clean, correct solution (step-by-step)
✅ Step 1: Stop and remove current Jenkins
docker stop jenkins
docker rm jenkins
✅ Step 2: Pull official Jenkins image with Docker CLI
docker pull jenkins/jenkins:lts
docker pull docker:dind
But instead of juggling images, we’ll build one clean image.
✅ Step 3: Create a custom Jenkins image with Docker installed
Dockerfile.jenkins
FROM jenkins/jenkins:lts
USER root
# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean
USER jenkins
✅ Step 4: Build Jenkins image
docker build -t jenkins-with-docker -f Dockerfile.jenkins .
✅ Step 5: Run Jenkins container (correctly)
docker run -d --name jenkins --user root -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins-with-docker
✅ Step 6: Verify (this time it WILL work)
docker exec -it jenkins docker ps
| Component     | Needed? | Why             |
| ------------- | ------- | --------------- |
| Docker Engine | ✅       | Runs containers |
| Docker Socket | ✅       | Communication   |
| Docker CLI    | ✅       | Issues commands |
| Jenkins       | ✅       | CI controller   |
