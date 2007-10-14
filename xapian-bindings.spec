Summary:	Bindings for the Xapian
Name:		xapian-bindings
Version:	1.0.3
Release:	%mkrel 1
License:	GPLv2
Group:		Development/Other
URL:		http://www.xapian.org
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	xapian-devel
%py_requires -d
BuildRequires:	php-devel
BuildRequires:	tcl-devel
BuildRequires:	java-devel
BuildRequires:	ruby-devel
BuildRequires:	mono-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
SWIG and JNI bindings allowing Xapian to be used from various 
other programming languages.

#%package java
#Summary:	Files needed for developing Java applications which use Xapian
#Group:		Development/Java
#Requires:	xapian >= %{version}
#Requires:	java

#%description java
#This package provides the files needed for developing Java applications which use Xapian.

%package mono
Summary:	Files needed for developing C# applications which use Xapian
Group:		Development/Other
Requires:	xapian >= %{version}
Requires:	mono

%description mono
This package provides the files needed for developing 
C# applications which use Xapian.

%package php
Summary:	Files needed for developing PHP scripts which use Xapian
Group:		Development/PHP
Requires:	xapian >= %{version}
Requires:	php-common

%description php
This package provides the files needed for developing 
PHP scripts which use Xapian.

%package python
Summary:	Files needed for developing Python scripts which use Xapian
Group:		Development/Python
Requires:	xapian >= %{version}
Requires:	python >= 2.5

%description python
This package provides the files needed for developing 
Python scripts which use Xapian.

%package ruby
Summary:	Files needed for developing Ruby applications which use Xapian
Group:		Development/Ruby
Requires:	xapian >= %{version}
Requires:	ruby

%description ruby
This package provides the files needed for developing 
Ruby applications which use Xapian.

%package tcl
Summary:	Files needed for developing TCL scripts which use Xapian
Group:		Development/Other
Requires:	xapian >= %{version}
Requires:	tcl

%description tcl
This package provides the files needed for developing 
TCL scripts which use Xapian.

%prep
%setup -q

%build
autoreconf --force

%configure2_5x \
	--with-csharp \
	--with-php \
	--with-python \
	--with-ruby \
	--with-tcl
#	--with-java

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

#%files
#%defattr(-,root,root)
#%doc AUTHORS ChangeLog COPYING NEWS README

#%files java
#%defattr(-,root,root)
#%{buildroot}/java/built/libxapian_jni.so

%files mono
%defattr(-,root,root)
%doc %{_docdir}/xapian-bindings/csharp
%{_libdir}/XapianSharp.la
%{_libdir}/XapianSharp.so
%{_libdir}/mono/XapianSharp/XapianSharp.dll
%{_libdir}/mono/gac/XapianSharp/%{version}*/XapianSharp.dll

%files php
%defattr(-,root,root)
%doc %{_docdir}/xapian-bindings/php
%{_libdir}/php/extensions/xapian.so
%{_datadir}/php5/xapian.php

%files python
%defattr(-,root,root)
%doc %{_docdir}/xapian-bindings/python
%{python_sitearch}/*.py*
%{python_sitearch}/*.so

%files ruby
%defattr(-,root,root)
%doc %{_docdir}/xapian-bindings/ruby
%{ruby_sitearchdir}/_xapian.so
%{ruby_sitelibdir}/xapian.rb

%files tcl
%defattr(-,root,root)
%doc %{_docdir}/xapian-bindings/tcl8
%{_prefix}/lib/xapian%{version}/pkgIndex.tcl
%{_prefix}/lib/xapian%{version}/xapian.so
