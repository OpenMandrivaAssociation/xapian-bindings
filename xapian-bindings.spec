Summary:	Bindings for the Xapian
Name:		xapian-bindings
Version:	1.0.6
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
URL:		http://www.xapian.org
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.bz2
Patch0:		xapian-bindings-1.0.5-ruby-docs-install.patch
BuildRequires:	xapian-devel >= %{version}
%py_requires -d
BuildRequires:	php-devel
BuildRequires:	php-cli
BuildRequires:	tcl-devel
BuildRequires:	java-rpmbuild
BuildRequires:	ruby-devel
BuildRequires:	mono-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SWIG and JNI bindings allowing Xapian to be used from various 
other programming languages.

%package java
Summary:	Files needed for developing Java applications which use Xapian
Group:		Development/Java
Requires:	xapian-core >= %{version}
Requires:	java-1.7.0-icedtea

%description java
This package provides the files needed for developing Java applications which
use Xapian.

%package mono
Summary:	Files needed for developing C# applications which use Xapian
Group:		Development/Other
Requires:	xapian-core >= %{version}
Requires:	mono

%description mono
This package provides the files needed for developing 
C# applications which use Xapian.

%package php
Summary:	Files needed for developing PHP scripts which use Xapian
Group:		Development/PHP
Requires:	xapian-core >= %{version}
Requires:	php-common

%description php
This package provides the files needed for developing 
PHP scripts which use Xapian.

%package python
Summary:	Files needed for developing Python scripts which use Xapian
Group:		Development/Python
Requires:	xapian-core >= %{version}
Requires:	python >= 2.5

%description python
This package provides the files needed for developing 
Python scripts which use Xapian.

%package ruby
Summary:	Files needed for developing Ruby applications which use Xapian
Group:		Development/Ruby
Requires:	xapian-core >= %{version}
Requires:	ruby

%description ruby
This package provides the files needed for developing 
Ruby applications which use Xapian.

%package tcl
Summary:	Files needed for developing TCL scripts which use Xapian
Group:		Development/Other
Requires:	xapian-core >= %{version}
Requires:	tcl

%description tcl
This package provides the files needed for developing 
TCL scripts which use Xapian.

%prep
%setup -q
%patch0 -p1

%build
# We want to avoid using jni.h from libgcj-devel, so we force
# the includedir instead of using ./configure detection, which would
# default to libgcj jni.h:
# - Anssi (12/2007)
export CPPFLAGS="-I%{java_home}/include"
export JDK_HOME=%{java_home}

%configure2_5x \
	--with-csharp \
	--with-php \
	--with-python \
	--with-ruby \
	--with-tcl \
	--with-java

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# Move to a proper location
install -d -m755 %{buildroot}%{_libdir}
mv %{buildroot}%{_builddir}/%{name}-%{version}/java/built/libxapian_jni.so %{buildroot}%{_libdir}

# Install the needed jar file as well
install -d -m755 %{buildroot}%{_jnidir}
install -m644 java/built/xapian_jni.jar %{buildroot}%{_jnidir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files java
%defattr(-,root,root)
%{_libdir}/libxapian_jni.so
%{_jnidir}/xapian_jni.jar

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
