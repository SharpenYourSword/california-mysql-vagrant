# vi: set ft=ruby

VAGRANTFILE_API_VERSION = "2"

SSH_PORT = 2233

Vagrant.require_version ">= 1.5.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "chef/ubuntu-14.04"

    # awkward fix for SSH reassignment issue (re-evaluate w/ Vagrant 1.5.4)
    config.vm.network :forwarded_port, guest: 22, host: 2223, id: "ssh", disabled: true
    config.vm.network :forwarded_port, guest: 22, host: SSH_PORT, auto_correct: true
    config.vm.define "mysql" do |mysql|
        config.vm.network "private_network", ip: "10.43.3.102"

        mysql.vm.provider "virtualbox" do |v|
            v.memory = 1024
            v.name = "ca-mysql-import"
        end

        mysql.vm.provision "ansible" do |ansible|
            ansible.playbook = "ansible/mysql.yml"
            ansible.limit = "all"
            # needed for common tasks to avoid EBS & checkout over synced_folders
            ansible.extra_vars = {deploy_type: "vagrant", ansible_ssh_user: 'vagrant'}
            # seems to avoid the delay with private IP not being available
            ansible.raw_arguments = ["-T 30"]
        end
    end
end
