%define name	autodia
%define Name	Autodia
%define version	2.08
%define release	%mkrel 1
%define _requires_exceptions perl(Inline::Java)

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Automatic Dia/UML generator
License:	    GPL
Group:		    Text tools
URL:		    http://www.aarontrevena.co.uk/opensource/autodia/
Source:		    http://search.cpan.org/CPAN/authors/id/T/TE/TEEJAY/%{Name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
AutoDia is a modular application that parses source code or data (if a
handler is available) and produces an XML document in Dia format,
essentially a Dia diagram autocreation package. The diagrams its creates
are standard UML diagrams showing dependencies, superclasses, packages,
classes and inheritances, as well as the methods, etc of each class. 

%prep
%setup -n %{Name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# what does script do there ?
rm -f %{buildroot}%{perl_vendorlib}/*.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING CREDITS FAQ README INSTALL TODO
%{_bindir}/*
%{perl_vendorlib}/%{Name}
%{perl_vendorlib}/%{Name}.pm
%{_mandir}/*/*
