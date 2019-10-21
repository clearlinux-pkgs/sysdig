#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysdig
Version  : 0.26.4
Release  : 23
URL      : https://github.com/draios/sysdig/archive/0.26.4.tar.gz
Source0  : https://github.com/draios/sysdig/archive/0.26.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: sysdig-bin = %{version}-%{release}
Requires: sysdig-data = %{version}-%{release}
Requires: sysdig-license = %{version}-%{release}
Requires: sysdig-man = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : buildreq-cmake
BuildRequires : c-ares-dev
BuildRequires : curl-dev
BuildRequires : elfutils-dev
BuildRequires : grpc-dev
BuildRequires : jq-dev
BuildRequires : jsoncpp-dev
BuildRequires : libb64-dev
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : protobuf-dev
BuildRequires : tbb-dev
BuildRequires : zlib-dev
Patch1: 0001-Fix-runtime-curses-error.patch
Patch2: 0001-PATCH-fix-build-with-LuaJIT-2.1-betas.patch

%description
sysdig
======
[![Build Status](https://travis-ci.org/draios/sysdig.png?branch=master)](https://travis-ci.org/draios/sysdig)

%package bin
Summary: bin components for the sysdig package.
Group: Binaries
Requires: sysdig-data = %{version}-%{release}
Requires: sysdig-license = %{version}-%{release}

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
%setup -q -n sysdig-0.26.4
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571623817
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DUSE_BUNDLED_DEPS=OFF -DBUILD_DRIVER=FALSE
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1571623817
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sysdig
cp %{_builddir}/sysdig-0.26.4/COPYING %{buildroot}/usr/share/package-licenses/sysdig/783f98f43ccc3ce8a369b86bcf5f769c9c83d678
cp %{_builddir}/sysdig-0.26.4/driver/GPL2.txt %{buildroot}/usr/share/package-licenses/sysdig/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/sysdig-0.26.4/userspace/sysdig/chisels/COPYING %{buildroot}/usr/share/package-licenses/sysdig/783f98f43ccc3ce8a369b86bcf5f769c9c83d678
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/share/bash-completion/completions/
mv %{buildroot}/usr/etc/bash_completion.d/sysdig %{buildroot}/usr/share/bash-completion/completions/sysdig
rm -rf %{buildroot}/usr/src
## install_append end

%files
%defattr(-,root,root,-)

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
/usr/share/sysdig/chisels/udp_extract.lua
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
/usr/share/package-licenses/sysdig/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/sysdig/783f98f43ccc3ce8a369b86bcf5f769c9c83d678

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/csysdig.8
/usr/share/man/man8/sysdig.8
