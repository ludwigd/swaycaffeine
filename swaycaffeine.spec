%global srcname swaycaffeine

Name:       swaycaffeine
Version:    0.0.1
Release:    1%{?dist}
Summary:    Easy access to Sway's idle inhibitors
License:    GPLv3+
URL: https://github.com/ludwigd/%{srcname}
# Sources can be obtained by
# git clone https://github.com/ludwigd/swaycaffeine
# cd swaycaffeine
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: python3
Requires: python3-i3ipc
Requires: sway

%description
Script for managing idle inhibitors in Sway.

%prep
%autosetup

%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 ./swaycaffeine %{buildroot}%{_bindir}/swaycaffeine

%files
%license LICENSE
%{_bindir}/swaycaffeine

%changelog
