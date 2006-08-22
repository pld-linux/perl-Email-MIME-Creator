#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Creator
Summary:	Email::MIME::Creator - Email::MIME constructor for starting a new part
Summary(pl):	Email::MIME::Creator - konstruktor dla Email::MIME do rozpoczêcia nowej czê¶ci
Name:		perl-Email-MIME-Creator
Version:	1.45
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	30fb0ce0b8b26317f258b283582067d5
URL:		http://search.cpan.org/dist/Email-MIME-Creator/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Date
BuildRequires:	perl-Email-MIME >= 1.82
BuildRequires:	perl-Email-MIME-Modifier >= 1.43
BuildRequires:	perl-Email-Simple >= 1.92
BuildRequires:	perl-Email-Simple-Creator >= 1.4
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::MIME::Creator is an Email::MIME constructor for starting a new
MIME part.

%description -l pl
Modu³ Email::MIME::Creator stanowi konstruktor dla Email::MIME do
rozpoczêcia nowej czê¶ci MIME wiadomo¶ci e-mail.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*
