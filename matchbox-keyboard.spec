#
# Conditional build:
%bcond_without	cairo	# use Xft backend instead of Cairo
#
Summary:	On-screen virtual keyboard
Summary(pl.UTF-8):	Wirtualna klawiatura na ekranie
Name:		matchbox-keyboard
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.yoctoproject.org/releases/matchbox/matchbox-keyboard/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	50940321d59fee23b38a4941100abf25
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-ru.patch
URL:		https://www.yoctoproject.org/software-item/matchbox/
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libfakekey-devel >= 0.1
BuildRequires:	pkgconfig
%if %{with cairo}
BuildRequires:	cairo-devel
%else
BuildRequires:	xorg-lib-libXft-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
matchbox-keyboard is an on screen 'virtual' or 'software' keyboard. It
will hopefully work well on various touchscreen devices from mobile
phones to tablet PCs running X Window System.

It aims to 'just work' supporting localised, easy to write XML layout
configuration files.

%description -l pl.UTF-8
matchbox-keyboard to "wirtualna" lub "programowa" klawiatura na
ekranie. Działa dobrze na różnych urządzeniach z ekranem dotykowym od
telefonów komórkowych do komputerów z tabletami z działającym systemem
X Window.

Program ma na celu "po prostu działać", obsługując zlokalizowane,
łatwe do napisania pliki XML konfigurujące układ klawiatury.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	%{?with_cairo:--enable-cairo}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/matchbox-keyboard
%{_datadir}/matchbox-keyboard
%{_desktopdir}/matchbox-keyboard.desktop
%{_pixmapsdir}/matchbox-keyboard.png
