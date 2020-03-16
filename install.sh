sudo yum update

# Install pip
sudo yum install -y python-pip

# Install GCC
sudo yum install -y gcc

# Install flask
sudo pip install flask
sudo pip install flask_session

sudo pip install werkzeug==0.16.1

# Install MySQL client
sudo yum install -y mysql

# Install MySQL Python library
sudo yum install -y mariadb-devel
sudo pip install mysqlclient
