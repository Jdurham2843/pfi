# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.define "postgres" do |postgres|
    postgres.vm.box = "ubuntu/xenial64"
    postgres.vm.provision "shell", path: "setupEnv/setupPostgres.sh"
    postgres.vm.network "forwarded_port", guest: 5432, host: 5432
  end
end
