#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	FastCGI
Summary:	Net::FastCGI -  FastCGI Toolkit
Summary(pl.UTF-8):	Net::FastCGI - Zestaw narzędzi FastCGI
Name:		perl-Net-FastCGI
Version:	0.14
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe8e232dc52053ce90c6f908049f2032
URL:		http://search.cpan.org/dist/Net-FastCGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution aims to provide a complete API for working with
the FastCGI protocol. The primary goal is to provide a function
oriented and object oriented API which are not tied to a specific I/O
model or framework. Secondary goal is to provide higher level
tools/API which can be used for debugging and interoperability
testing.

%description -l pl.UTF-8
Ten pakiet dostarcza kompletne API do pracy z protokołem FastCGI.
Podstawowym jego celem jest dostarczenie funkcyjnego i obiektowego API
nie powiązanego z żadnym konkretnym modelem komunikacyjnym.
Drugorzędnym celem jest dostarczenie narzędzi wyższego poziomu do
celów diagnostycznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Net/FastCGI{,/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/FastCGI.pm
%{perl_vendorlib}/Net/FastCGI
%{_mandir}/man3/Net::FastCGI*.3pm*
%{_examplesdir}/%{name}-%{version}
