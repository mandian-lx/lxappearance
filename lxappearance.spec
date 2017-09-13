Summary:	A new feature-rich GTK+ theme switcher
Name:		lxappearance
Version:	0.6.3 
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXAppearance
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
#Patch0:		po.fuzzy.patch

BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	xsltproc

Suggests:	%{name}-obconf

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXAppearance is the standard theme switcher of LXDE. Users are able to
change the theme, icons, and fonts used by applications easily. Starting at
version 0.6.1 it also allows to enable the accessibility features.

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/lxappearance.*

#---------------------------------------------------------------------------

%package devel
Summary:	%{name} developement files
Group:		Graphical desktop/Other

%description devel
This package contains header files needed when building applications based on
%{name}.

%files devel
%doc COPYING TODO
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# .desktop
desktop-file-install --vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

# locales
%find_lang %{name}

