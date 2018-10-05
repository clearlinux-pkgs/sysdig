#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysdig
Version  : 0.24.0
Release  : 17
URL      : https://github.com/draios/sysdig/archive/0.24.0.tar.gz
Source0  : https://github.com/draios/sysdig/archive/0.24.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sysdig-bin = %{version}-%{release}
Requires: sysdig-data = %{version}-%{release}
Requires: sysdig-license = %{version}-%{release}
Requires: sysdig-man = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : elfutils-dev
BuildRequires : jq-dev
BuildRequires : jsoncpp-dev
BuildRequires : libb64-dev
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : tbb-dev
BuildRequires : zlib-dev
Patch1: 0001-Fix-runtime-curses-error.patch

%description
sysdig
======
[![Build Status](https://travis-ci.org/draios/sysdig.png?branch=master)](https://travis-ci.org/draios/sysdig)

%package bin
Summary: bin components for the sysdig package.
Group: Binaries
Requires: sysdig-data = %{version}-%{release}
Requires: sysdig-license = %{version}-%{release}
Requires: sysdig-man = %{version}-%{release}

%description bin
bin components for the sysdig package.


%package data
Summary: data components for the sysdig package.
Group: Data

%description data
data components for the sysdig package.


%package license
Summary: license components for the sysdig package.
Group: Default

%description license
license components for the sysdig package.


%package man
Summary: man components for the sysdig package.
Group: Default

%description man
man components for the sysdig package.


%prep
%setup -q -n sysdig-0.24.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538702947
mkdir -p clr-build
pushd clr-build
%cmake .. -DUSE_BUNDLED_DEPS=OFF -DBUILD_DRIVER=FALSE
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1538702947
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sysdig
cp COPYING %{buildroot}/usr/share/package-licenses/sysdig/COPYING
cp userspace/sysdig/chisels/COPYING %{buildroot}/usr/share/package-licenses/sysdig/userspace_sysdig_chisels_COPYING
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/share/bash-completion/completions/
mv %{buildroot}/usr/etc/bash_completion.d/sysdig %{buildroot}/usr/share/bash-completion/completions/sysdig
## install_append end

%files
%defattr(-,root,root,-)
/usr/src/sysdig-0.1.1dev/Makefile
/usr/src/sysdig-0.1.1dev/bpf/Makefile
/usr/src/sysdig-0.1.1dev/bpf/bpf_helpers.h
/usr/src/sysdig-0.1.1dev/bpf/filler_helpers.h
/usr/src/sysdig-0.1.1dev/bpf/fillers.h
/usr/src/sysdig-0.1.1dev/bpf/maps.h
/usr/src/sysdig-0.1.1dev/bpf/plumbing_helpers.h
/usr/src/sysdig-0.1.1dev/bpf/probe.c
/usr/src/sysdig-0.1.1dev/bpf/quirks.h
/usr/src/sysdig-0.1.1dev/bpf/ring_helpers.h
/usr/src/sysdig-0.1.1dev/bpf/types.h
/usr/src/sysdig-0.1.1dev/dkms.conf
/usr/src/sysdig-0.1.1dev/driver_config.h
/usr/src/sysdig-0.1.1dev/dynamic_params_table.c
/usr/src/sysdig-0.1.1dev/event_table.c
/usr/src/sysdig-0.1.1dev/fillers_table.c
/usr/src/sysdig-0.1.1dev/flags_table.c
/usr/src/sysdig-0.1.1dev/main.c
/usr/src/sysdig-0.1.1dev/ppm.h
/usr/src/sysdig-0.1.1dev/ppm_compat_unistd_32.h
/usr/src/sysdig-0.1.1dev/ppm_cputime.c
/usr/src/sysdig-0.1.1dev/ppm_events.c
/usr/src/sysdig-0.1.1dev/ppm_events.h
/usr/src/sysdig-0.1.1dev/ppm_events_public.h
/usr/src/sysdig-0.1.1dev/ppm_fillers.c
/usr/src/sysdig-0.1.1dev/ppm_fillers.h
/usr/src/sysdig-0.1.1dev/ppm_flag_helpers.h
/usr/src/sysdig-0.1.1dev/ppm_ringbuffer.h
/usr/src/sysdig-0.1.1dev/ppm_syscall.h
/usr/src/sysdig-0.1.1dev/syscall_table.c

%files bin
%defattr(-,root,root,-)
/usr/bin/csysdig
/usr/bin/sysdig
/usr/bin/sysdig-probe-loader

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/sysdig
/usr/share/sysdig/chisels/COPYING
/usr/share/sysdig/chisels/ansiterminal.lua
/usr/share/sysdig/chisels/around.lua
/usr/share/sysdig/chisels/bottlenecks.lua
/usr/share/sysdig/chisels/common.lua
/usr/share/sysdig/chisels/dkjson.lua
/usr/share/sysdig/chisels/echo_fds.lua
/usr/share/sysdig/chisels/fdbytes_by.lua
/usr/share/sysdig/chisels/fdcount_by.lua
/usr/share/sysdig/chisels/fdtime_by.lua
/usr/share/sysdig/chisels/fileslower.lua
/usr/share/sysdig/chisels/flame.lua
/usr/share/sysdig/chisels/http.lua
/usr/share/sysdig/chisels/httplog.lua
/usr/share/sysdig/chisels/httptop.lua
/usr/share/sysdig/chisels/iobytes.lua
/usr/share/sysdig/chisels/iobytes_file.lua
/usr/share/sysdig/chisels/iobytes_net.lua
/usr/share/sysdig/chisels/list_login_shells.lua
/usr/share/sysdig/chisels/lscontainers.lua
/usr/share/sysdig/chisels/lsof.lua
/usr/share/sysdig/chisels/memcachelog.lua
/usr/share/sysdig/chisels/netlower.lua
/usr/share/sysdig/chisels/netstat.lua
/usr/share/sysdig/chisels/proc_exec_time.lua
/usr/share/sysdig/chisels/ps.lua
/usr/share/sysdig/chisels/scallslower.lua
/usr/share/sysdig/chisels/shellshock_detect.lua
/usr/share/sysdig/chisels/spectrogram.lua
/usr/share/sysdig/chisels/spy_file.lua
/usr/share/sysdig/chisels/spy_ip.lua
/usr/share/sysdig/chisels/spy_logs.lua
/usr/share/sysdig/chisels/spy_port.lua
/usr/share/sysdig/chisels/spy_syslog.lua
/usr/share/sysdig/chisels/spy_users.lua
/usr/share/sysdig/chisels/statsd.lua
/usr/share/sysdig/chisels/stderr.lua
/usr/share/sysdig/chisels/stdin.lua
/usr/share/sysdig/chisels/stdout.lua
/usr/share/sysdig/chisels/subsecoffset.lua
/usr/share/sysdig/chisels/table_generator.lua
/usr/share/sysdig/chisels/topconns.lua
/usr/share/sysdig/chisels/topcontainers_cpu.lua
/usr/share/sysdig/chisels/topcontainers_error.lua
/usr/share/sysdig/chisels/topcontainers_file.lua
/usr/share/sysdig/chisels/topcontainers_net.lua
/usr/share/sysdig/chisels/topfiles_bytes.lua
/usr/share/sysdig/chisels/topfiles_errors.lua
/usr/share/sysdig/chisels/topfiles_time.lua
/usr/share/sysdig/chisels/topports_server.lua
/usr/share/sysdig/chisels/topprocs_cpu.lua
/usr/share/sysdig/chisels/topprocs_errors.lua
/usr/share/sysdig/chisels/topprocs_file.lua
/usr/share/sysdig/chisels/topprocs_net.lua
/usr/share/sysdig/chisels/topscalls.lua
/usr/share/sysdig/chisels/topscalls_time.lua
/usr/share/sysdig/chisels/tracers_2_statsd.lua
/usr/share/sysdig/chisels/v_backlog.lua
/usr/share/sysdig/chisels/v_connections.lua
/usr/share/sysdig/chisels/v_containers.lua
/usr/share/sysdig/chisels/v_containers_errors.lua
/usr/share/sysdig/chisels/v_cpus.lua
/usr/share/sysdig/chisels/v_directories.lua
/usr/share/sysdig/chisels/v_docker_events.lua
/usr/share/sysdig/chisels/v_errors.lua
/usr/share/sysdig/chisels/v_file_opens.lua
/usr/share/sysdig/chisels/v_files.lua
/usr/share/sysdig/chisels/v_incoming_connections.lua
/usr/share/sysdig/chisels/v_io_by_type.lua
/usr/share/sysdig/chisels/v_kubernetes_controllers.lua
/usr/share/sysdig/chisels/v_kubernetes_deployments.lua
/usr/share/sysdig/chisels/v_kubernetes_namespaces.lua
/usr/share/sysdig/chisels/v_kubernetes_pods.lua
/usr/share/sysdig/chisels/v_kubernetes_replicasets.lua
/usr/share/sysdig/chisels/v_kubernetes_services.lua
/usr/share/sysdig/chisels/v_marathon_apps.lua
/usr/share/sysdig/chisels/v_marathon_groups.lua
/usr/share/sysdig/chisels/v_mesos_frameworks.lua
/usr/share/sysdig/chisels/v_mesos_tasks.lua
/usr/share/sysdig/chisels/v_notifications.lua
/usr/share/sysdig/chisels/v_page_faults.lua
/usr/share/sysdig/chisels/v_port_bindings.lua
/usr/share/sysdig/chisels/v_procs.lua
/usr/share/sysdig/chisels/v_procs_cpu.lua
/usr/share/sysdig/chisels/v_procs_errors.lua
/usr/share/sysdig/chisels/v_procs_fd_usage.lua
/usr/share/sysdig/chisels/v_slow_io.lua
/usr/share/sysdig/chisels/v_spans_list.lua
/usr/share/sysdig/chisels/v_spans_summary.lua
/usr/share/sysdig/chisels/v_spectro_all.lua
/usr/share/sysdig/chisels/v_spectro_file.lua
/usr/share/sysdig/chisels/v_spectro_traces.lua
/usr/share/sysdig/chisels/v_sports.lua
/usr/share/sysdig/chisels/v_spy_syslog.lua
/usr/share/sysdig/chisels/v_spy_users.lua
/usr/share/sysdig/chisels/v_spy_users_wsysdig.lua
/usr/share/sysdig/chisels/v_syscall_procs.lua
/usr/share/sysdig/chisels/v_syscalls.lua
/usr/share/sysdig/chisels/v_threads.lua
/usr/share/sysdig/chisels/v_traces_list.lua
/usr/share/sysdig/chisels/v_traces_summary.lua
/usr/share/sysdig/chisels/wsysdig_summary.lua
/usr/share/zsh/site-functions/_sysdig
/usr/share/zsh/vendor-completions/_sysdig

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sysdig/COPYING
/usr/share/package-licenses/sysdig/userspace_sysdig_chisels_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/csysdig.8
/usr/share/man/man8/sysdig.8
