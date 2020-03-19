#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spelling
Version  : 2.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/spelling_2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spelling_2.1.tar.gz
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

%description
and description files. Includes utilities to automate checking of documentation and 
    vignettes as a unit test during 'R CMD check'. Both British and American English are 
    supported out of the box and other languages can be added. In addition, packages may
    define a 'wordlist' to allow custom terminology without having to abuse punctuation.

%prep
%setup -q -c -n spelling

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569295298

%install
export SOURCE_DATE_EPOCH=1569295298
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spelling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spelling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spelling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spelling || :


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
