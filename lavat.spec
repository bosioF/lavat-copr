Name:           lavat
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lava lamp simulation in the terminal

License:        MIT
URL:            https://github.com/bosioF/lavat-copr
Source0:        https://github.com/bosioF/lavat-copr/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A quaint little program that simulates a lava lamp in the terminal 
using metaballs and termbox2.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/lavat

%changelog
* Sat Jul 11 2026 b0510 - 1.4.0-1
- Initial packaging for Fedora Copr
