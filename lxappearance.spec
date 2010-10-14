Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.5.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://downloads.sourceforge.net/project/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel desktop-file-utils
BuildRequires:	intltool

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

desktop-file-install --vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%buildroot%_datadir/applications %buildroot%_datadir/applications/*.desktop

rm -fr %buildroot{%_includedir/lxappearance,%_libdir/pkgconfig/*.pc}



%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post  
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
