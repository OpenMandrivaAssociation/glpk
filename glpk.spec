%define major	36
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	GLPK glpsol utility
Name:		glpk
Version:	4.52.1
Release:	36
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://www.gnu.org/software/glpk/glpk.html
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gmp-devel
BuildRequires:	tetex-latex
BuildRequires:	texinfo

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP),
and other related problems. It is a set of routines written in ANSI C
and organized in the form of a callable library.

This package contains the utility glpsol.

%package -n %{libname}
Summary:	GLPK shared libraries
Group:		Sciences/Mathematics

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with GLPK.

%package -n %{devname}
Summary:	Header files for development with GLPK
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}glpk-static-devel < %{version}-%{release} 

%description -n %{devname}
This package contains the headers needed to develop applications using
GLPK.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

# Trust Knuth to produce a single-pass compiler for a multiple-pass language.
pushd doc
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex && \
pdflatex -interaction=nonstopmode -file-line-error-style glpk.tex
texi2pdf -p gmpl.texi && \
popd

%install
%makeinstall
# Clean out the examples directory so we can include it wholesale in %doc.
%make -C examples distclean
rm -rf examples/Makefile*

%files 
%{_bindir}/glpsol

%files -n %{libname}
%{_libdir}/libglpk.so.%{major}*

%files -n %{devname}
%doc examples doc/*.txt doc/*.pdf AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_includedir}/*.h
%{_libdir}/*.so


