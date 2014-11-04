Name:       lipstick-recorder

Summary:    Lipstick recorder client
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    GPLv2
URL:        https://bitbucket.org/jolla/lipstick-jolla-home
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-qtwayland-wayland_egl-devel

%description
Lipstick recorder client

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
make %{_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%attr(755, root, privileged) %{_bindir}/lipstick-recorder
