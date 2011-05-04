Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.5.0
Release:	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://downloads.sourceforge.net/project/lxde/%name-%version.tar.gz
#Patch0:		02_font_config.patch
Patch1:		01_gtk3_migration.patch
#Patch2:		20_lang_lxappearance.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel desktop-file-utils
BuildRequires:	intltool
Suggests: lxappearance-obconf

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%package devel
Group:		Graphical desktop/Other
Summary:	%{name} developement files
Provides:	%{name}-devel = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q
#%patch0 -p1 -b .add_font_antialiasing_control
%patch1 -p1 -b .fix_GTK3_build
#%patch2 -p1 -b .lang_plugin

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


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc
