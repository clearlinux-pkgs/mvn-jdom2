#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jdom2
Version  : 2.0.5
Release  : 2
URL      : https://github.com/hunterhacker/jdom/archive/JDOM-2.0.5.tar.gz
Source0  : https://github.com/hunterhacker/jdom/archive/JDOM-2.0.5.tar.gz
Source1  : https://repo1.maven.org/maven2/org/jdom/jdom2/2.0.5/jdom2-2.0.5.jar
Source2  : https://repo1.maven.org/maven2/org/jdom/jdom2/2.0.5/jdom2-2.0.5.pom
Source3  : https://repo1.maven.org/maven2/org/jdom/jdom2/2.0.6/jdom2-2.0.6.jar
Source4  : https://repo1.maven.org/maven2/org/jdom/jdom2/2.0.6/jdom2-2.0.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 Saxpath
Requires: mvn-jdom2-data = %{version}-%{release}

%description
ABOUT
Cobertura is a free Java code coverage reporting tool.  It is
based on jcoverage 1.0.5.  See the Cobertura web page for more
details.  http://cobertura.sourceforge.net/

%package data
Summary: data components for the mvn-jdom2 package.
Group: Data

%description data
data components for the mvn-jdom2 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5/jdom2-2.0.5.jar
/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.5/jdom2-2.0.5.pom
/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6/jdom2-2.0.6.jar
/usr/share/java/.m2/repository/org/jdom/jdom2/2.0.6/jdom2-2.0.6.pom
