Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.5.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://downloads.sourceforge.net/project/lxde/%name-%version.tar.gz
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

%build
./autogen.sh
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

rm -fr %{buildroot}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc
