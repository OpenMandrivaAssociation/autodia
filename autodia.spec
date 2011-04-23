%define upstream_name	 Autodia
%define upstream_version 2.10

Name:       autodia
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Automatic Dia/UML generator
License:	GPL
Group:		Text tools
Url:		http://www.aarontrevena.co.uk/opensource/autodia/
Source0:    http://search.cpan.org/CPAN/authors/id/T/TE/TEEJAY/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
AutoDia is a modular application that parses source code or data (if a
handler is available) and produces an XML document in Dia format,
essentially a Dia diagram autocreation package. The diagrams its creates
are standard UML diagrams showing dependencies, superclasses, packages,
classes and inheritances, as well as the methods, etc of each class. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/*
%{_mandir}/*/*
