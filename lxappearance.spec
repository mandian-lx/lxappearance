Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel desktop-file-utils

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post  
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
%{_mandir}/man1/*
