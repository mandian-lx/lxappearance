Summary:	A new feature-rich GTK+ theme switcher
Name:     	lxappearance
Version:	0.5.1
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0: 	http://downloads.sourceforge.net/project/lxde/%{name}-%version.tar.gz
Patch0:		po.fuzzy.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
Suggests: 	lxappearance-obconf

%description
LXAppearance is a new GTK+ theme switcher developed for project LXDE.

%package devel
Summary:	%{name} developement files
Group:		Graphical desktop/Other
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains header files needed when building applications based on
%{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install --vendor="" \
	--remove-key="NotShowIn" \
	--add-only-show-in="LXDE" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/lxappearance.*

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lxappearance.pc

