#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: 1ab68ca
#
Name     : R-spelling
Version  : 2.3.0
Release  : 55
URL      : https://cran.r-project.org/src/contrib/spelling_2.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spelling_2.3.0.tar.gz
Summary  : Tools for Spell Checking in R
Group    : Development/Tools
License  : MIT
Requires: R-commonmark
Requires: R-hunspell
Requires: R-knitr
Requires: R-xml2
BuildRequires : R-commonmark
BuildRequires : R-hunspell
BuildRequires : R-knitr
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and description files. Includes utilities to automate checking of documentation and 
    vignettes as a unit test during 'R CMD check'. Both British and American English are 
    supported out of the box and other languages can be added. In addition, packages may
    define a 'wordlist' to allow custom terminology without having to abuse punctuation.

%prep
%setup -q -n spelling
pushd ..
cp -a spelling buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709658978

%install
export SOURCE_DATE_EPOCH=1709658978
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spelling/DESCRIPTION
/usr/lib64/R/library/spelling/INDEX
/usr/lib64/R/library/spelling/LICENSE
/usr/lib64/R/library/spelling/Meta/Rd.rds
/usr/lib64/R/library/spelling/Meta/features.rds
/usr/lib64/R/library/spelling/Meta/hsearch.rds
/usr/lib64/R/library/spelling/Meta/links.rds
/usr/lib64/R/library/spelling/Meta/nsInfo.rds
/usr/lib64/R/library/spelling/Meta/package.rds
/usr/lib64/R/library/spelling/NAMESPACE
/usr/lib64/R/library/spelling/NEWS
/usr/lib64/R/library/spelling/R/spelling
/usr/lib64/R/library/spelling/R/spelling.rdb
/usr/lib64/R/library/spelling/R/spelling.rdx
/usr/lib64/R/library/spelling/WORDLIST
/usr/lib64/R/library/spelling/help/AnIndex
/usr/lib64/R/library/spelling/help/aliases.rds
/usr/lib64/R/library/spelling/help/paths.rds
/usr/lib64/R/library/spelling/help/spelling.rdb
/usr/lib64/R/library/spelling/help/spelling.rdx
/usr/lib64/R/library/spelling/html/00Index.html
/usr/lib64/R/library/spelling/html/R.css
/usr/lib64/R/library/spelling/templates/spelling.Rout.save
/usr/lib64/R/library/spelling/tests/spelling.R
